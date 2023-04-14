"""main package"""
import sys
import argparse
import os
import re


def parse_args():
    """
    Parses command-line arguments using the argparse module.

    Returns:
    - args: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='''
            The htmlpack module can be used to help preprocess HTML files 
            for production environments.
            It can be used to strip HTML comments, minify HTML, and more.
            ''')
    parser.add_argument('-s', '--strip-comments', action='store_true',
                        help='Whether to strip HTML comments (default: False)')
    parser.add_argument('-v', '--verbose', action='store_true',
                    help='Verbose output (default: False)')
    parser.add_argument('-d', '--dry-run', action='store_true',
                    help='Perform a dry run without modifying files (default: False)')
    parser.add_argument('path', type=str,
                        help='Path to file or folder')
    args = parser.parse_args()
    return args


def remove_comments(file_path, args):
    """
    Removes HTML comments from the given file.

    Args:
    - file_path: The path to the file to be processed.
    - args: The parsed command-line arguments.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    # Use a regex to remove HTML comments
    pattern = r'<!--(.*?)-->'
    if args.verbose or args.dry_run:
        subs = re.findall(pattern, content, flags=re.DOTALL)
        print(
            f"{'Identified' if args.dry_run else 'Removing'} {len(subs)} comments from {file_path}"
        )
        for comment in subs:
            print(f"* <!--{comment}-->" )

    if not args.dry_run:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(content)


def process_file(file_path, args):
    """
    Processes the given file.

    Args:
    - file_path: The path to the file to be processed.
    - args: The parsed command-line arguments.
    """
    if args.strip_comments:
        remove_comments(file_path, args)


def process_folder(folder_path, args):
    """
    Processes all the files in the given folder.

    Args:
    - folder_path: The path to the folder to be processed.
    - strip_comments: Whether to strip HTML comments from the files.
    """
    valid_extensions = ['.html', '.hbs']
    for root, _dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file_path)[1]
            if ext in valid_extensions:
                process_file(file_path, args)


def main():
    """
    The main function that is called when the module is run from the command-line.
    """
    args = parse_args()
    path = args.path

    if os.path.isfile(path):
        process_file(path, args)
    elif os.path.isdir(path):
        process_folder(path, args)
    else:
        sys.exit(f"{path} is not a valid file or folder.")

