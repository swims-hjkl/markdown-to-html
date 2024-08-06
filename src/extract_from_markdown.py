import re


def extract_markdown_images(text):
    regex_pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex_pattern, text)
    return matches


def extract_markdown_links(text):
    regex_pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex_pattern, text)
    return matches


if __name__ == "__main__":
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
