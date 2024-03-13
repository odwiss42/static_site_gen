from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(text={self.text}, text_type={self.text_type}, url={self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == text_type_text:
            return LeafNode(None,self.text)
        elif self.text_type == text_type_bold:
            return LeafNode('b',self.text)
        elif self.text_type == text_type_italic:
            return LeafNode('i', self.text)
        elif self.text_type == text_type_code:
            return LeafNode('code', self.text)
        elif self.text_type == text_type_link:
            return LeafNode('a', self.text, props={'href':self.url})
        elif self.text_type == text_type_image:
            return LeafNode('img',"",props={"src":self.url, "alt":self.text})
        else:
            raise TypeError(f"Invalid text node type: {self.text_type}")