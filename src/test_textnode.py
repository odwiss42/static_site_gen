import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(text=This is a text node, text_type=text, url=https://www.boot.dev)", repr(node)
        )
    
    def test_tnthtml_txt(self):
        txt_node = TextNode("This is a text node", text_type_text)
        lf_node = LeafNode(None,"This is a text node")
        self.assertEqual(txt_node.text_node_to_html_node(), lf_node)
    
    def test_tnthtml_bold(self):
        txt_node = TextNode("This is bold text", text_type_bold)
        lf_node = LeafNode("b","This is bold text")
        self.assertEqual(txt_node.text_node_to_html_node(), lf_node)

    def test_tnthtml_italic(self):
        txt_node = TextNode("This is italic text", text_type_italic)
        lf_node = LeafNode("i","This is italic text")
        self.assertEqual(txt_node.text_node_to_html_node(), lf_node)

    def test_tnthtml_txt(self):
        txt_node = TextNode("This is code", text_type_code)
        lf_node = LeafNode('code',"This is code")
        self.assertEqual(txt_node.text_node_to_html_node(), lf_node)

    def test_tnthtml_link(self):
        txt_node = TextNode("This is a link", text_type_link, 'https://www.boot.dev')
        lf_node = LeafNode('a',"This is a link",props={'href':txt_node.url})
        self.assertEqual(txt_node.text_node_to_html_node(), lf_node)

    def test_tnthtml_img(self):
        txt_node = TextNode("This is an image", text_type_image, 'https://www.boot.dev/boots.jpg')
        lf_node = LeafNode('img',"",props={"src":txt_node.url, "alt":txt_node.text})
        self.assertEqual(txt_node.text_node_to_html_node(), lf_node)

    

if __name__ == "__main__":
    unittest.main()