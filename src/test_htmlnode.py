import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        html_node = HtmlNode("<a>", "this is a link", None, {
                             "href": "www.google.com",
                             "target": "_blank"})
        expected = ' href="www.google.com" target="_blank"'
        self.assertEqual(expected, html_node.props_to_html())

    def test_none(self):
        html_node = HtmlNode()
        self.assertEqual(None, html_node.tag)
        self.assertEqual(None, html_node.value)
        self.assertEqual(None, html_node.children)
        self.assertEqual(None, html_node.props)
