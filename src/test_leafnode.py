from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):

    def test_no_value(self):
        no_value_leaf_node = LeafNode(None, None, None)
        self.assertRaises(ValueError, no_value_leaf_node.to_html)

    def test_no_tag(self):
        no_tag_leaf_node = LeafNode(
            "this is the value", None, props={"font-style": "bold"})
        self.assertEqual("this is the value", no_tag_leaf_node.to_html())

    def test_tag(self):
        no_tag_leaf_node = LeafNode(
            "this is the value", tag="p", props={"font-style": "bold"})
        self.assertEqual(
            '<p font-style="bold">this is the value</p>',
            no_tag_leaf_node.to_html()
        )
