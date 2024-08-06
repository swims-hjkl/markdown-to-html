from textnode import TextNode
from extract_from_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        split_text = node.text.split(delimiter, maxsplit=2)
        if node.text_type != "text" or len(split_text) == 1:
            result.append(node)
            continue
        left, mid, right = split_text
        result.append(TextNode(left, "text", None))
        result.append(TextNode(mid, text_type, None))
        if len(right) > 0:
            result.extend(split_nodes_delimiter(
                [TextNode(right, "text", None)], delimiter, text_type))

    return result


def _split_node_by_image(old_node):
    result = []
    matches = extract_markdown_links(old_node.text)
    if not matches:
        return [old_node]
    match = matches[0]
    match_original = f"![{match[0]}]({match[1]})"
    split_text = old_node.text.split(match_original, maxsplit=1)
    if len(split_text) == 1:
        return [old_node]
    left, right = split_text
    result.append(TextNode(
        left, "text", None))
    result.append(TextNode(
        match[0], "image", match[1]))
    if len(right) > 0:
        result.extend(_split_node_by_image(TextNode(right, "text", None)))
    return result


def _split_node_by_link(old_node):
    result = []
    matches = extract_markdown_links(old_node.text)
    if not matches:
        return [old_node]
    match = matches[0]
    match_original = f"[{match[0]}]({match[1]})"
    split_text = old_node.text.split(match_original, maxsplit=1)
    if len(split_text) == 1:
        return [old_node]
    left, right = split_text
    result.append(TextNode(
        left, "text", None))
    result.append(TextNode(
        match[0], "link", match[1]))
    if len(right) > 0:
        result.extend(_split_node_by_link(TextNode(right, "text", None)))
    return result


def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            result.append(old_node)
            continue
        result.extend(_split_node_by_image(old_node))
    return result


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            result.append(old_node)
            continue
        result.extend(_split_node_by_link(old_node))
    return result


def text_to_text_node(text_node):
    nodes = split_nodes_delimiter([text_node], "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
