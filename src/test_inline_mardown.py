import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    split_nodes_image,
    extract_markdown_links,
    split_nodes_link,
    text_to_textnodes
)
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_md_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png) end"
        images = extract_markdown_images(text)
        expected = [('image','https://i.imgur.com/zjjcJKZ.png'),('another','https://i.imgur.com/dfsdkjfd.png')]
        self.assertEqual(images,expected)

    def test_extract_md_links(self):
        text = "This is text with a [link](https://meatspin.com) and [another](https://logicalincrements.com) end"
        links = extract_markdown_links(text)
        expected = [('link','https://meatspin.com'),('another','https://logicalincrements.com')]
        self.assertEqual(links,expected)

    def test_split_nodes_image_1(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png) end"
        node = TextNode(text,text_type_text)
        expected = [
            TextNode('This is text with an ',text_type_text),
            TextNode('image',text_type_image,url='https://i.imgur.com/zjjcJKZ.png'),
            TextNode(' and ', text_type_text),
            TextNode('another',text_type_image,url='https://i.imgur.com/dfsdkjfd.png'),
            TextNode(' end', text_type_text)
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_node_link_1(self):
        text = "This is text with a [link](https://meatspin.com) and [another](https://logicalincrements.com) end"
        node = TextNode(text,text_type_text)
        expected = [
            TextNode('This is text with a ',text_type_text),
            TextNode('link',text_type_link,url='https://meatspin.com'),
            TextNode(' and ', text_type_text),
            TextNode('another',text_type_link,url='https://logicalincrements.com'),
            TextNode(' end', text_type_text)
        ]
        self.assertEqual(split_nodes_link([node]),expected)

    def test_text_to_textnode(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)'
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text),expected)

    

if __name__ == "__main__":
    unittest.main()