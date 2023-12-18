import os
import json
import argparse
import subprocess
import git

from project_info_class import ProjectInfo

structure = json.load(open("structure_template.json", "r"))


def logo():
    return """
╔═╗┬ ┬┌┬┐┌─┐╔═╗┌┬┐┬─┐┬ ┬┌─┐┌┬┐
╠═╣│ │ │ │ │╚═╗ │ ├┬┘│ ││   │ 
╩ ╩└─┘ ┴ └─┘╚═╝ ┴ ┴└─└─┘└─┘ ┴ 
   ------------------------
       ----------------
           --------    
"""


def start():
    print(logo())
    print("Welcome to AutoStruct template generator!")
    print("------------------------------------------")
    print("Please enter the following information:")
    print("------------------------------------------")
    # name = input("1. Project name: ")
    # scope = input("2. Project scope ([Data] or Script): ")
    # repo_name = input("3. Repository name: ")
    author_name = os.system('git config --global --get user.name')
    author = f"4. Author name: {author_name}"
    print(author)
    # description = input("5. Description: ")
    # open_license = input("6. Open source license: ")
    # print("------------------------------------------")
    #
    # info = ProjectInfo(
    #     project_name=name,
    #     scope=scope,
    #     repo_name=repo_name,
    #     author_name=author,
    #     description=description,
    #     open_source_license=open_license,
    # )

    # print(info.get_project_name())
    # print(info.get_repo_name())
    # print(info.get_author_name())
    # print(info.get_project_name())
    # print(info.get_description())
    # print(info.get_open_source_license())
    # print(info.__str__())


if __name__ == "__main__":
    start()
