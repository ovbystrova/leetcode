from bs4 import BeautifulSoup
import json
from pathlib import Path
import requests
from typing import Any, Dict

from tqdm import tqdm
import yaml


def get_submissions(
        submissions_url: str,
        offset: int,
        limit: int,
        last_key: str,
        cookies: Dict[str, str]
):
    """
    Geet all submissions from user and return only accepted ones.
    :param submissions_url:
    :param offset:
    :param limit:
    :param last_key:
    :param cookies:
    :return:
    """
    # Keep track of all submissions
    all_submissions = []
    while True:
        # Send a GET request to the LeetCode submissions API
        url = submissions_url.format(offset, limit, last_key or "")
        response = requests.get(url, cookies=cookies)

        # Parse the JSON response
        submissions = json.loads(response.content.decode("utf-8"))

        # If there are no more submissions, break out of the loop
        if "submissions_dump" not in submissions:
            break

        # Keep only accepted submissions
        accepted_submissions = [submission for submission in submissions["submissions_dump"]
                                if submission["status_display"] == "Accepted"]
        all_submissions.extend(accepted_submissions)

        # Set the last submission key for the next fetch
        # Update the offset for the next fetch
        last_key = submissions["last_key"]
        offset += limit

    return all_submissions, last_key


def get_task_submission_data(
        submission,
        task_url: str
):
    """
    Get relevant data (title, number, difficulty, tags, etc.) from submission and LeetCode problem.
    :param submission:
    :param task_url: str
    :return:
    """
    data = {}

    task_response = requests.get(task_url)
    task_soup = BeautifulSoup(task_response.content, "html.parser")

    task_json = json.loads(str(task_soup.find('script', {'id': '__NEXT_DATA__'}).string))
    difficulty = task_json['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['question'][
        'difficulty']
    tags = task_json["props"]["pageProps"]["dehydratedState"]["queries"][8]["state"]["data"]["question"]["topicTags"]
    tags = [x["name"] for x in tags]

    data["code"] = submission["code"]
    data["title"] = submission["title"]
    data["title_full"] = task_soup.find("div", class_="h-full").find("span", class_="text-label-1").text.strip()
    data["task_number"] = int(data["title_full"].split(".")[0])
    data["difficulty"] = difficulty
    data["tags"] = tags
    data["filepath"] = data["title_full"].replace(". ", ".").replace(" ", "_") + ".py"

    return data


def update_readme(
        filepath,
        data: Dict[str, Any],
        task_url: str
):
    """
    Read README.md file and add new submissions to the table.
    :param filepath:
    :param data:
    :param task_url:
    :return:
    """

    with open(filepath) as f:
        readme_data = f.read()

    tags = "".join([f"<li>{tag}</li>" for tag in data["tags"]])
    raw = f"| {data['task_number']} |" \
          f" [{data['title']}]({task_url}) | " \
          f"[Python]({data['filepath']}) |" \
          f" {data['difficulty']} | {tags} |"

    # insert new rows into README.md table
    readme_data_upd = readme_data + "\n" + raw

    # write updated contents back to README.md file
    with open(submission_dir / "README.md", "w") as f:
        f.write(readme_data_upd)


if __name__ == "__main__":

    config_file = "./resources/config.yaml"
    config = yaml.safe_load(
        open(config_file, encoding='utf-8')
    )

    request = config["request"]
    submissions_api_url = request["url"] + request["url_submissions"]
    with open(request["cookie_file"]) as f:
        cookies = {"LEETCODE_SESSION": f.read()}

    # Get problems that were downloaded earlier
    with open(config["processed_links"]) as f:
        links_processed = [link.strip("\n") for link in f.readlines()]
    print(f"There are {len(links_processed)} processed links.")

    # Get the last submission key from the previous fetch (if any)
    last_key = None
    if Path(config["last_key"]).exists():
        with open(config["last_key"], "r") as f:
            last_key = f.read().strip()

    # Keep track of all submissions
    submissions, last_key = get_submissions(
        submissions_url=submissions_api_url,
        offset=request["offset"],
        limit=request["limit"],
        last_key=last_key,
        cookies=cookies
    )
    with open(config["last_key"], "w") as f:
        f.write(last_key)
    print(f"Got {len(submissions)} submissions to process")

    for submission in tqdm(submissions):
        task_id = submission["title_slug"]
        task_url = request["url"] + "/problems/" + task_id + "/"
        submission_url = request["url"] + submission["url"]
        if task_url in links_processed:
            continue

        # Get relevant fields from submission and leetcode task
        try:
            data = get_task_submission_data(
                submission=submission,
                task_url=task_url
            )
        except:
            print(f"Error {task_url}. Skipping")
            continue

        # Choose directory where to save new task
        task_number = data["task_number"]
        if task_number <= 500:
            submission_dir = Path(config["download_dir"]) / "1-500"
        elif 500 < task_number <= 1000:
            submission_dir = Path(config["download_dir"]) / "501-1000"
        else:
            submission_dir = Path(config["download_dir"]) / "1001-"

        # Save submission code to python file
        with open(submission_dir / data["filepath"], "w") as f:
            f.write(data["code"])

        # Update processed links
        links_processed.append(task_url)

        # Update readme file
        update_readme(
            filepath=submission_dir / "README.md",
            data=data,
            task_url=task_url
        )

    with open(config["processed_links"], "w") as f:
        for line in links_processed:
            f.write(line + "\n")
    print(f"All done.")
