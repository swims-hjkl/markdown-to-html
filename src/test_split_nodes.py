import unittest

from textnode import TextNode
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):

    def test_code(self):
        text_node1 = TextNode("asjd`this is code`asd", "text", None)
        text_node2 = TextNode("asjd*this is italic text*asd", "text", None)
        text_node4 = TextNode("this is bold text", "bold", None)
        text_node5 = TextNode("this is italic text", "italic", None)
        result = split_nodes_delimiter(
            [text_node1, text_node2, text_node4, text_node5],
            '`', "code")
        expected_result = [TextNode("asjd", "text", None),
                           TextNode("this is code", "code", None), TextNode(
                           "asd", "text", None),
                           text_node2, text_node4, text_node5]
        self.assertEqual(result,
                         expected_result)
        expected_result = [TextNode("asjd", "text", None),
                           TextNode("this is code", "code", None),
                           TextNode("asd", "text", None),
                           TextNode("asjd", "text", None),
                           TextNode("this is italic text", "italic", None),
                           TextNode("asd", "text", None),
                           text_node4, text_node5]
        result = split_nodes_delimiter(result, '*', 'italic')
        self.assertEqual(sorted(result, key=lambda k: k.text), sorted(
            expected_result, key=lambda k: k.text))

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "image", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode(
                "to youtube", "image", "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(sorted(new_nodes, key=lambda k: k.text), sorted(
            expected, key=lambda k: k.text))
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to boot dev](https://www.boot.dev)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "image", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode(
                "to boot dev", "image", "https://www.boot.dev"
            ),
        ]
        self.assertEqual(sorted(new_nodes, key=lambda k: k.text), sorted(
            expected, key=lambda k: k.text))

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode(
                "to youtube", "link", "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(sorted(new_nodes, key=lambda k: k.text), sorted(
            expected, key=lambda k: k.text))
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        node2 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        new_nodes = split_nodes_link([node, node2])
        expected = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode(
                "to youtube", "link", "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode(
                "to youtube", "link", "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(sorted(new_nodes, key=lambda k: k.text), sorted(
            expected, key=lambda k: k.text))
