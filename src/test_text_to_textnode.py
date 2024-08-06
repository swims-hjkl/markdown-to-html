import unittest

from textnode import TextNode
import split_nodes


class TestTextToTextNode(unittest.TestCase):

    def test_text_to_text_node(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and another ![obi wan image 2](https://i.imgur.com/fJRm4Vk.jpeg)  and a [link](https://boot.dev) with another *italic text 2*"
        result = split_nodes.text_to_text_node(
            TextNode(text, "text"))
        expected = [TextNode("This is ", "text", None), TextNode("text", "bold", None), TextNode(" with an ", "text", None), TextNode("italic", "italic", None),
                    TextNode(" word and a ", "text", None), TextNode("code block", "code", None), TextNode(" and an ", "text", None), TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and another ", "text", None), TextNode("obi wan image 2", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode("  and a ", "text", None), TextNode("link", "link", "https://boot.dev"), TextNode(" with another ", "text", None), TextNode("italic text 2", "italic", None)]
        self.assertListEqual(expected, result)
