

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        str_to_return = f'{type(self).__name__}('
        for att, att_value in vars(self).items():
            if type(att_value) is str:
                str_to_return += f'{att}="{att_value}", '
            else:
                str_to_return += f'{att}={att_value}, '
        return str_to_return.rstrip(', ') + ')'
    
    def __eq__(self,other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def to_html(self):
        raise NotImplementedError("This should be implemented by Subclasses")
    
    def props_to_html(self):
        html_props = ""
        for (key, value) in self.props.items():
            html_props += key + '="' + value +'" '
        return html_props.rstrip()
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"