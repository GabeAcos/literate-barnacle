from textnode import *
from htmlnode import *
from markdown_blocks import *
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


def extract_title(markdown):
    lines = markdown.split("\n")
    head = []
    for line in lines:
        if line.startswith("# "):
            head.append(line[2:].strip())
    return head[0]


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_file = f.read()
    with open(template_path, "r") as f:
        template_file = f.read()

    htmlnode = markdown_to_html_node(markdown_file)
    content = htmlnode.to_html()
    title = extract_title(markdown_file)
    template_file = template_file.replace(r"{{ Content }}", content)
    template_file = template_file.replace(r"{{ Title }}", title)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_file)


def main():
    clear_public()
    copy_static("static/")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
