import re
from pathlib import Path
from typing import Union

SEARCH_DIR = Path("../solutions")
README_FILE = "README.md"
LINK_PATTERN = r"\((https:.*?)\)"


def get_links_from_file(
        filepath: Union[str, Path]
):
    """
    Extract all links to leetcode problems from filepath
    :param filepath: path to README.md file
    :return: List of leetcode links
    """
    with open(filepath, "r") as f:
        text = f.read()
    links = re.findall(LINK_PATTERN, text)
    return links


if __name__ == "__main__":

    files = [file for file in SEARCH_DIR.rglob(f"{README_FILE}") if file.is_file()]
    print(f"Found {len(files)} files")
    links = list()
    for filepath in files:
        links_update = get_links_from_file(filepath)
        links.extend(links_update)

    print(f"Saving {len(links)} links")
    with open("resources/downloaded_links.txt", "w") as f:
        for link in links:
            f.write(link + "\n")
