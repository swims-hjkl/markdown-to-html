import unittest


from blocks import markdown_to_blocks, block_to_block_type


class TestBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):

        text = """
               # This is a heading

               This is a paragraph of text. It has some **bold** and *italic* words inside of it.


               * This is the first list item in a list block
               * This is a list item
               * This is another list item
               """
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(expected, markdown_to_blocks(text))

    def test_block_to_block_type(self):
        block = "# this is a heading"
        self.assertEqual("heading", block_to_block_type(block))
        block = "### this is a heading"
        self.assertEqual("heading", block_to_block_type(block))
        block = "###### this is a heading"
        self.assertEqual("heading", block_to_block_type(block))
        block = "######this is a heading"
        self.assertEqual("paragraph", block_to_block_type(block))
        block = "```this is a heading\nakjsdhaksd\nakjhiencmen\nasdj```"
        self.assertEqual("code", block_to_block_type(block))
        block = "* this is a heading\n* akjsdhaksd\n- akjhiencmen\n- asdj```"
        self.assertEqual("unordered_list", block_to_block_type(block))
        block = "1. this is a heading\n2. akjsdhaksd\n3. akjhiencmen\n4. asdj"
        self.assertEqual("ordered_list", block_to_block_type(block))
        block = "1. this is a heading\n2. akjsdhaksd\n3. akjhiencmen\n3. asdj"
        self.assertEqual("paragraph", block_to_block_type(block))
