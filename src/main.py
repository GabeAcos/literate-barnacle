from textnode import *
from htmlnode import *
import os
import shutil

PUBLIC_PATH = "public"


def copy_static(path):
    # print(f"path: {path}")
    for dir in os.listdir(path):
        current_path = os.path.join(path, dir)
        # print(f"current path: {current_path}")
        if not os.path.isfile(current_path):
            dir_path = current_path.replace("static", "public")
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            # print(f"not a file: {current_path}")
            copy_static(current_path)
        else:
            file_path = os.path.join(path, dir)
            # print(f"file path: {file_path}")
            public = file_path.replace("static", "public")
            # print(f"file: {public}")
            shutil.copy(file_path, public)
            continue


def clear_public():
    # check if public folder exists, if it does, delete and recreate it
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
        os.mkdir(PUBLIC_PATH)
    else:
        os.mkdir(PUBLIC_PATH)


def main():
    clear_public()
    copy_static("static/")


if __name__ == "__main__":
    main()
