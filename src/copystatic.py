import os
import shutil

def copy_tree(source_folder, destination_folder, verbose=True):
    if not os.path.exists(source_folder):
        raise ValueError("Source path does not exist")
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    source_content = os.listdir(source_folder)
    for content in source_content:
        content_path = os.path.join(source_folder, content)
        destination_path = os.path.join(destination_folder, content)
        if os.path.isfile(content_path):
            shutil.copy(content_path, destination_path)
            if verbose:
                print(f'copied {content_path} to {destination_path}')
        else:
            copy_tree(content_path, destination_path)