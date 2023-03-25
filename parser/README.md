# Leetcode Submissions Parser


To get all problem links from repository you can run:
```shell
python get_downloaded_links.py
```
This will save [`downloaded_links.txt`](resources/downloaded_links.txt) to `resources` folder with all links that are present in repository.

To update your repository with new accepted submissions you can run:
```shell
python update_sumbissions.py
```

Requred parameters should be filled to [config.yaml](resources/config.yaml) file.
Authorization is made with `resources/cookies.txt`


This parser: 
1) Reads already downloaded submissions
2) Extracts new submissions from your LeetCode profile
3) Saves code to *.py files following the repo structure
4) Updates README.md files 

***!!!Manual Review is required after running the script!!!***.

*This parser was made with the assistance of ChatGPT model.*
