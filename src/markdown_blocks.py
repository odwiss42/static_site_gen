from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode

block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'codeblock'
block_type_quote = 'quote'
block_type_ulist = 'ulist'
block_type_list = 'list'

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    blocks = [block.strip('\n ') for block in split_blocks if block != '']
    return blocks

def block_to_block_type(markdown_block):
    headings = ('# ',
                '## ',
                '### ',
                '#### ',
                '##### ',
                '###### ')
    if markdown_block.startswith(headings):
        return block_type_heading
    if markdown_block.startswith('```') and markdown_block.endswith('```'):
        return block_type_code
    lines = markdown_block.split('\n')
    if all(map(lambda line: line.startswith('>'), lines)):
        return block_type_quote
    if (all(map(lambda line: line.startswith('-'), lines)) or
            all(map(lambda line: line.startswith('*'), lines))):
        return block_type_ulist
    if all(map(lambda line : len(line) > 1, lines)):
        line_starts = [line[0] for line in lines]
        point_check = [line[1] for line in lines]
        if all(map(lambda char: char == '.', point_check)):
            if sorted(line_starts) == line_starts:
                return block_type_list
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node.text_node_to_html_node()
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level > 6:
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_list:
        return list_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

def markdown_to_html_node(markdown_doc):
    blocks = markdown_to_blocks(markdown_doc)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)