
from textnode import TextNode
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode):
    if not isinstance(text_node, TextNode):
        raise ValueError("text_node should be of type TextNode")
    if text_node.text_type == "text":
        return LeafNode(text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(value=text_node.text, tag="b")
    elif text_node.text_type == "italic":
        return LeafNode(value=text_node.text, tag="i")
    elif text_node.text_type == "code":
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.text_type == "link":
        return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("The given text node is not supported")


if __name__ == "__main__":
    print(text_node_to_html_node(TextNode("alt text", "image", "url")).to_html())
