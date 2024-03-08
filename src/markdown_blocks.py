block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'codeblock'
block_type_quote = 'quote'
block_type_unordered_list = 'unolist'
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
        return block_type_unordered_list
    if all(map(lambda line : len(line) > 1, lines)):
        line_starts = [line[0] for line in lines]
        point_check = [line[1] for line in lines]
        if all(map(lambda char: char == '.', point_check)):
            if sorted(line_starts) == line_starts:
                return block_type_list
    return block_type_paragraph
    