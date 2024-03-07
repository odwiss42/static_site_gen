import unittest
from htmlnode import (HTMLNode, LeafNode, ParentNode)


class TestHTMLNode(unittest.TestCase):
    def test_eq_no_att(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_eq_0(self):
        node1 = HTMLNode("p","this is a paragraph")
        node2 = HTMLNode("p","this is a paragraph")
        self.assertEqual(node1, node2)

    def test_neq_0(self):
        node1 = HTMLNode("p","this is a paragraph")
        node2 = HTMLNode("a","this is a hyperlink", props={"href": "https://www.google.com"})
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node1 = HTMLNode("a","this is a hyperlink", props={"href": "https://www.google.com"})
        node_repr = 'HTMLNode(tag="a", value="this is a hyperlink", children=None, props={\'href\': \'https://www.google.com\'})'
        self.assertEqual(node_repr, repr(node1))

    def test_props_to_html(self):
        node1 = HTMLNode("a","this is a hyperlink", props={"href": "https://www.google.com", "target": "_blank"})
        pth = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(pth, node1.props_to_html())

    def test_eq(self):
        node1 = LeafNode("a", "Click me!", {'href': 'https://www.google.com'})
        node2 = LeafNode("a", "Click me!", {'href': 'https://www.google.com'})
        self.assertEqual(node1,node2) 

    def test_to_html(self):
        node1 = LeafNode("a", "Click me!", {'href': 'https://www.google.com'})
        to_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(to_html, node1.to_html())
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()