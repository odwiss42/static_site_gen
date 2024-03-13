from markdown_blocks import *
import os

def extract_title(markdown):
    lines = markdown.split('\n')
    header = list(filter(lambda line: line.startswith('# '), lines))
    if not header:
        raise Exception('No h1 header in markdown file')
    elif len(header) > 1 :
        raise Exception('File has more than one header')
    return header[0]

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown_text = ''
    with open(from_path, 'r') as f:
        markdown_text = f.read()
    template = ''
    with open(template_path, 'r') as t:
        template = t.read()
    html_text = markdown_to_html_node(markdown_text).to_html()
    page_title = extract_title(markdown_text)
    template = template.replace("{{ Title }}", page_title)
    page = template.replace("{{ Content }}", html_text)

    path_dir = os.path.dirname(dest_path)
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    if not os.path.exists(dest_path):
        open(dest_path, 'x')
    with open(dest_path, 'w') as f:
        f.write(page)
        f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError("Source path does not exist")
    source_content = os.listdir(dir_path_content)
    for content in source_content:
        from_path = os.path.join(dir_path_content, content)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_dir_path + '/index.html')
        else:
            to_path = os.path.join(dest_dir_path, content)
            generate_pages_recursive(from_path, template_path, to_path)
