import unittest

from convertors import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode


class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_exception(self):
        text_node = TextNode("something", text_type="something")
        self.assertRaises(Exception, text_node_to_html_node, text_node)

    def test_text(self):
        text_node = TextNode("something", text_type="text")
        expected_leaf_node = LeafNode(value="something")
        self.assertEqual(text_node_to_html_node(text_node), expected_leaf_node)

    def test_bold(self):
        text_node = TextNode("something", text_type="bold")
        expected_leaf_node = LeafNode(value="something", tag="b")
        self.assertEqual(text_node_to_html_node(text_node), expected_leaf_node)

    def test_italic(self):
        text_node = TextNode("something", text_type="italic")
        expected_leaf_node = LeafNode(value="something", tag="i")
        self.assertEqual(text_node_to_html_node(text_node), expected_leaf_node)

    def test_code(self):
        text_node = TextNode("something", text_type="code")
        expected_leaf_node = LeafNode(value="something", tag="code")
        self.assertEqual(text_node_to_html_node(text_node), expected_leaf_node)

    def test_image(self):
        text_node = TextNode("something", text_type="image", url="image_url")
        expected_leaf_node = LeafNode(value="", tag="img", props={
                                      "src": "image_url", "alt": "something"})
        self.assertEqual(text_node_to_html_node(text_node), expected_leaf_node)

    def test_link(self):
        text_node = TextNode("anchor text",
                             text_type="link", url="link_url")
        expected_leaf_node = LeafNode(
            value="anchor text", tag="a", props={"href": "link_url"})
        self.assertEqual(text_node_to_html_node(text_node), expected_leaf_node)
