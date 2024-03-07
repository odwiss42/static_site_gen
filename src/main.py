from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode)


def main():
    node1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode("a", "Click me!", props={"href": "https://www.google.com"}),
        ],
    )
    node2 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode("a", "Click me!", props={"href": "https://www.google.com"}),
        ],
    )
    node3 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    nested_node = ParentNode("p",[node1,node2,node3])

    print(nested_node.to_html())
    
main()