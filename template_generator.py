import os
import json
import argparse
from project_info_class import ProjectInfo

structure = json.load(open("structure_template.json", "r"))


def logo():
    return """
╔═╗┬ ┬┌┬┐┌─┐╔═╗┌┬┐┬─┐┬ ┬┌─┐┌┬┐
╠═╣│ │ │ │ │╚═╗ │ ├┬┘│ ││   │ 
╩ ╩└─┘ ┴ └─┘╚═╝ ┴ ┴└─└─┘└─┘ ┴ 

"""


def start():
    print("Welcome to AutoStruct template generator!")
    print("------------------------------------------")
    print("Please enter the following information:")
    print("------------------------------------------")
    name = input("1. Project name: ")
    repo_name = input("2. Repository name: ")
    author = input("3. Author name: ")
    description = input("4. Description: ")
    open_license = input("5. Open source license: ")
    print("------------------------------------------")
    # print("Please enter your choice: ")

    info = ProjectInfo(
        project_name=name,
        repo_name=repo_name,
        author_name=author,
        description=description,
        open_source_license=open_license,
    )

    # print(info.get_project_name())
    # print(info.get_repo_name())
    # print(info.get_author_name())
    # print(info.get_project_name())
    # print(info.get_description())
    # print(info.get_open_source_license())
    print(info.__str__())


if __name__ == "__main__":
    print(logo())
    start()
