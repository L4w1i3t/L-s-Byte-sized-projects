import os
import sys

# List of directories to ignore
IGNORE_DIRS = {
    '__pycache__',
    '.git',
    'node_modules',
    'venv',
    'env',
    '.venv',
    'build',
    'dist',
    'logs',
    '.pytest_cache',
    '.mypy_cache',
    '.tox',
    '.idea',
    '.vscode',
    '.DS_Store',
    '*.egg-info',
    'npm-debug.log',
    'yarn-error.log',
    '.hg',
    '.svn'
}

def generate_file_tree(directory, prefix="", code_extensions=None, exclude_extensions=None, ignore_files=None):
    """
    Recursively generates a file tree string for the given directory.
    Includes contents of code files based on specified extensions.

    Args:
        directory (str): The directory path to scan.
        prefix (str): Current prefix for indentation.
        code_extensions (set): Set of file extensions considered as code files.
        exclude_extensions (set): Set of file extensions to exclude.
        ignore_files (set): Specific filenames to ignore.

    Returns:
        str: The formatted file tree with optional file contents.
    """
    if code_extensions is None:
        code_extensions = {
            '.py', '.js', '.java', '.c', '.cpp', '.cs', '.html', '.css',
            '.rb', '.go', '.php', '.swift', '.kt', '.ts', '.json', '.xml',
            '.yaml', '.yml', '.sql', '.sh', '.bash', '.zsh', '.ini', '.md',
            '.vue'
        }
    if exclude_extensions is None:
        exclude_extensions = {
            '.pyc', '.pyo', '.class', '.o', '.exe', '.dll', '.so', '.dylib'
        }
    if ignore_files is None:
        ignore_files = {}

    # Check for treeignore.txt and read its contents
    treeignore_path = os.path.join(directory, 'treeignore.txt')
    if os.path.exists(treeignore_path):
        with open(treeignore_path, 'r', encoding='utf-8') as f:
            ignored_entries = f.read().splitlines()
            ignore_files.update(ignored_entries)

    file_tree = ""
    entries = list(os.scandir(directory))
    entries = [entry for entry in entries if entry.name not in IGNORE_DIRS and entry.name not in ignore_files]
    entry_count = len(entries)

    for i, entry in enumerate(entries):
        connector = "├── " if i < entry_count - 1 else "└── "

        if entry.is_dir():
            file_tree += f"{prefix}{connector}[{entry.name}]/\n"
            extension = "│   " if i < entry_count - 1 else "    "
            file_tree += generate_file_tree(entry.path, prefix + extension, code_extensions, exclude_extensions, ignore_files)
        else:
            _, ext = os.path.splitext(entry.name)
            ext = ext.lower()

            # Skip excluded file types
            if ext in exclude_extensions:
                continue

            file_tree += f"{prefix}{connector}{entry.name}\n"

            # If the file is a code file, include its contents
            if ext in code_extensions:
                try:
                    with open(entry.path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Prepare the content with proper indentation
                    content_lines = content.splitlines()
                    indented_content = '\n'.join([f"{prefix}    {line}" for line in content_lines])
                    # Append the content to the file tree
                    file_tree += f"{prefix}    --- Start of {entry.name} ---\n"
                    file_tree += f"{indented_content}\n"
                    file_tree += f"{prefix}    --- End of {entry.name} ---\n"
                except Exception as e:
                    file_tree += f"{prefix}    [Could not read file: {e}]\n"

    return file_tree

def create_file_tree_txt(directory):
    """
    Creates a 'file_tree_with_code_contents.txt' in the specified directory containing the file tree
    and contents of code files.

    Args:
        directory (str): The directory path where the file tree will be created.
    """
    print(f"Generating file tree for directory: {directory}")
    
    # Dynamically determine filenames to ignore
    script_name = os.path.basename(__file__)
    ignore_files = {script_name, "file_tree_with_code_contents.txt", "create_tree.py", "file_tree.txt", "create_tree_and_get_contents.exe", "create_tree.exe"}
    
    file_tree = generate_file_tree(directory, ignore_files=ignore_files)
    file_name = os.path.join(directory, "file_tree_with_code_contents.txt")
    
    try:
        with open(file_name, "w", encoding='utf-8') as file:
            file.write(file_tree)
        print(f"File tree successfully created and saved as 'file_tree_with_code_contents.txt' in {directory}")
    except Exception as e:
        print(f"Failed to write file_tree_with_code_contents.txt: {e}")

if __name__ == "__main__":
    # Determine the directory where the .exe or .py file is located
    if getattr(sys, 'frozen', False):
        # If the script is run as a bundled executable (e.g., PyInstaller )
        current_directory = os.path.dirname(sys.executable)
    else:
        # If the script is run as a standard .py file
        current_directory = os.path.dirname(os.path.abspath(__file__))

    create_file_tree_txt(current_directory)