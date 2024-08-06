import os
import shutil
from pathlib import Path

import markdown_to_html

SOURCE_FOLDER = "./static"
DESTINATION_FOLDER = "./public"


def copy_files(source_folder=SOURCE_FOLDER,
               destination_folder=DESTINATION_FOLDER):
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    for element in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, element)):
            shutil.copy(os.path.join(source_folder, element),
                        os.path.join(destination_folder, element))
        else:
            copy_files(source_folder=os.path.join(source_folder, element),
                       destination_folder=os.path.join(destination_folder, element))


def delete_fodler_and_recreate(folder_name=DESTINATION_FOLDER):
    shutil.rmtree(folder_name)
    os.mkdir("public")


def extract_title(markdown: str):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line.strip("# ")
    raise Exception("title not present")


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html_content = markdown_to_html.markdown_to_html(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for element in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, element)
        dest_full_path = os.path.join(dest_dir_path, element)
        if os.path.isfile(full_path) and Path(full_path).suffix == ".md":
            generate_page(full_path, template_path,
                          dest_full_path.replace(".md", ".html"))
        else:
            generate_pages_recursive(
                full_path, template_path, dest_full_path)


def main():
    delete_fodler_and_recreate()
    copy_files()
    generate_pages_recursive(
        "content", "template.html", "public")


main()
