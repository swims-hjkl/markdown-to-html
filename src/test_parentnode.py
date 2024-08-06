import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_multiple_children(self):

        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text"),
            ],
            None
        )
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html()
        )

    def test_parent_inside_parent(self):

        parent_node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b")
            ],
            {"font-style": "bold"}
        )
        node = ParentNode(
            "div",
            [
                parent_node,
                LeafNode("italic text", "i")
            ],
            None
        )
        self.assertEqual(
            '<div><p font-style="bold"><b>Bold text</b></p><i>italic text</i></div>',
            node.to_html()
        )

    def test_no_children(self):

        node = ParentNode(
            "div",
            None,
            None
        )

        self.assertRaises(ValueError, node.to_html)
