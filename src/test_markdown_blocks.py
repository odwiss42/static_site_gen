import unittest
from markdown_blocks import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_md_to_blocks(self):
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""

        excepted = [
            'This is **bolded** paragraph',
            """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
            """* This is a list
* with items""",
        ]

        self.assertEqual(markdown_to_blocks(text),excepted)

    def test_btbt_paragraph_1(self):
        block = """random text
another line
and another gfdkausdnlasmndasmlasjdlasmdmasd"""
        expected = block_type_paragraph
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_paragraph_2(self):
        block = """1.random text
2another line
3.and another gfdkausdnlasmndasmlasjdlasmdmasd"""
        expected = block_type_paragraph
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_paragraph_3(self):
        block = """1.random text
3.another line
2.and another gfdkausdnlasmndasmlasjdlasmdmasd"""
        expected = block_type_paragraph
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_list_1(self):
        block = """1.random text
2.another line
3.and another gfdkausdnlasmndasmlasjdlasmdmasde"""
        expected = block_type_list
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_list_2(self):
        block = """* random text
* another line
* and another gfdkausdnlasmndasmlasjdlasmdmasde"""
        expected = block_type_unordered_list
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_list_3(self):
        block = """* random text
- another line
* and another gfdkausdnlasmndasmlasjdlasmdmasde"""
        expected = block_type_paragraph
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_code(self):
        block = """```random code
>another line
and another gfdkausdnlasmndasmlasjdlasmdmasde```"""
        expected = block_type_code
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_quote(self):
        block = """>random quote
>another line
>and another gfdkausdnlasmndasmlasjdlasmdmasde"""
        expected = block_type_quote
        self.assertEqual(block_to_block_type(block),expected)

    def test_btbt_heading_1(self):
        blocks = ['# level 1 heading',
                  '## level 2 heading',
                  '### level 3 heading',
                  '#### level 4 heading',
                  '##### level 5 heading',
                  '###### level 6 heading',]
        for block in blocks:
            self.assertEqual(block_to_block_type(block),block_type_heading)
        
    def test_btbt_heading_2(self):
        blocks = ['#not a heading',
                  '####### not a heading',
                  ' # not a heading']
        for block in blocks:
            self.assertEqual(block_to_block_type(block),block_type_paragraph)


if __name__ == "__main__":
    unittest.main()