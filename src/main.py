from copystatic import copy_tree
from page_generator import generate_page, generate_pages_recursive


def main():
    copy_tree('./static', './public')
    generate_pages_recursive('./content',
                             './template.html',
                             './public')

main()