

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        repr = f'{type(self).__name__}('
        for att, att_value in vars(self).items():
            if type(att_value) is str:
                repr += f'{att}="{att_value}", '
            else:
                repr += f'{att}={att_value}, '
        return repr.rstrip(', ') + ')'
    
    def __eq__(self,other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def to_html(self):
        raise NotImplementedError('This should be implemented by Subclasses')
    
    def props_to_html(self):
        html_props = ' '
        if self.props is None:
            return ''
        for (key, value) in self.props.items():
            html_props += key + '="' + value +'" '
        return html_props.rstrip()
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Invalid HTML: no value')
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('Invalid HTML: no tag')
        if self.children is None:
            raise ValueError('Invalid HTML: this is a parent node, so it should contain children')
        opening_tag = f'<{self.tag}{self.props_to_html()}>'
        closing_tag = f'</{self.tag}>'
        body = ''
        for child in self.children:
            body += child.to_html()
        return opening_tag + body + closing_tag