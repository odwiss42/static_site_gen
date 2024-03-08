import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, bold section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        split_nodes= []
        sections = []    
        for alt_text, link in images:
            tmp_split = node_text.split(f"![{alt_text}]({link})", 1)
            sections.append(tmp_split[0])
            sections.append((alt_text, link))
            node_text = tmp_split[1]
        sections.append(node_text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i][0], text_type_image, sections[i][1]))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        split_nodes= []
        sections = []    
        for alt_text, link in links:
            tmp_split = node_text.split(f"[{alt_text}]({link})", 1)
            sections.append(tmp_split[0])
            sections.append((alt_text, link))
            node_text = tmp_split[1]
        sections.append(node_text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i][0], text_type_link, sections[i][1]))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    initial_node = TextNode(text, text_type_text)
    text_nodes = split_nodes_delimiter([initial_node], '**', text_type_bold)
    text_nodes = split_nodes_delimiter(text_nodes, '*', text_type_italic)
    text_nodes = split_nodes_delimiter(text_nodes, '`', text_type_code)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes