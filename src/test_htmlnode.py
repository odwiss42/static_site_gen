import unittest
from htmlnode import (HTMLNode, LeafNode)


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
        pth = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(pth, node1.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("a", "Click me!", {'href': 'https://www.google.com'})
        node2 = LeafNode("a", "Click me!", {'href': 'https://www.google.com'})
        self.assertEqual(node1,node2) 

    def test_to_html(self):
        node1 = LeafNode("a", "Click me!", {'href': 'https://www.google.com'})
        to_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(to_html, node1.to_html())

if __name__ == "__main__":
    unittest.main()