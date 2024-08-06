import unittest

import extract_from_markdown


class TestExtractFromMarkdown(unittest.TestCase):

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_from_markdown.extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"),
                    ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertListEqual(
            sorted(result, key=lambda k: k[0]), sorted(
                expected, key=lambda k: k[0])
        )

    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_from_markdown.extract_markdown_links(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                    ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(
            sorted(result, key=lambda k: k[0]), sorted(
                expected, key=lambda k: k[0])
        )
