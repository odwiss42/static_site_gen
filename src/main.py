from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image
)



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

    txt_node = TextNode("This is an image", text_type_image, 'https://www.boot.dev/boots.jpg')
    print(txt_node.text_node_to_html_node())

    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    print(extract_markdown_images(text))

    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text)) 
    
    node7 = TextNode(text1,text_type_text)
    print(split_nodes_image([node7]))

main()