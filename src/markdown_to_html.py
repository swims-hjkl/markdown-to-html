from blocks import markdown_to_blocks, block_to_block_type

from textnode import TextNode
from htmlnode import HtmlNode
from split_nodes import text_to_text_node
from convertors import text_node_to_html_node


def markdown_to_html(markdown):

    output_html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            text_nodes = text_to_text_node(
                TextNode(block.split("# ")[1], "text"))
            child_html_nodes = [text_node_to_html_node(
                text_node) for text_node in text_nodes]
            number = block.count("#")
            html_node = HtmlNode(tag=f"h{number}", children=child_html_nodes)
            output_html_nodes.append(html_node)
        if block_type == "code":
            text_nodes = text_to_text_node(
                TextNode('\n'.join(block.split("\n")[1: -1]), "text"))
            child_html_nodes = [text_node_to_html_node(
                text_node) for text_node in text_nodes]
            html_node = HtmlNode(tag="code", children=child_html_nodes)
            pre_html_node = HtmlNode(tag="pre", children=[html_node])
            output_html_nodes.append(pre_html_node)
        if block_type == "quote":
            text = ""
            for line in block.split("\n"):
                text = text + line[2:]
            text_nodes = text_to_text_node(TextNode(text, "text"))
            child_html_nodes = [text_node_to_html_node(
                text_node) for text_node in text_nodes]
            html_node = HtmlNode(tag="blockquote", children=child_html_nodes)
            output_html_nodes.append(html_node)
        if block_type == "unordered_list":
            unordered_list_html_item = HtmlNode(tag="ul", children=[])
            for index, line in enumerate(block.split("\n")):
                list_item_html_node = HtmlNode(tag="li")
                line = line[2:]
                text_nodes = text_to_text_node(TextNode(line, "text"))
                html_nodes = [text_node_to_html_node(
                    text_node) for text_node in text_nodes]
                list_item_html_node.children = html_nodes
                unordered_list_html_item.children.append(list_item_html_node)
            output_html_nodes.append(unordered_list_html_item)
        if block_type == "ordered_list":
            ordered_list_html_item = HtmlNode(tag="ol", children=[])
            for index, line in enumerate(block.split("\n")):
                list_item_html_node = HtmlNode(tag="li")
                line = line.replace(f"{index + 1}. ", "")
                text_nodes = text_to_text_node(TextNode(line, "text"))
                html_nodes = [text_node_to_html_node(
                    text_node) for text_node in text_nodes]
                list_item_html_node.children = html_nodes
                ordered_list_html_item.children.append(list_item_html_node)
            output_html_nodes.append(ordered_list_html_item)
        if block_type == "paragraph":
            text_nodes = text_to_text_node(TextNode(block, "text"))
            html_nodes = [text_node_to_html_node(
                text_node) for text_node in text_nodes]
            paragraph_html_node = HtmlNode(tag="p", children=html_nodes)
            output_html_nodes.append(paragraph_html_node)
    return HtmlNode(tag="div", children=output_html_nodes)
