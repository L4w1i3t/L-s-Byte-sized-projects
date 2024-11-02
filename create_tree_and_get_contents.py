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

def generate_file_tree(directory, level=0, code_extensions=None, exclude_extensions=None):
    """
    Recursively generates a file tree string for the given directory.
    Includes contents of code files based on specified extensions.

    Args:
        directory (str): The directory path to scan.
        level (int): Current depth level for indentation.
        code_extensions (set): Set of file extensions considered as code files.
        exclude_extensions (set): Set of file extensions to exclude.

    Returns:
        str: The formatted file tree with optional file contents.
    """
    if code_extensions is None:
        code_extensions = {
            '.py', '.js', '.java', '.c', '.cpp', '.cs', '.html', '.css',
            '.rb', '.go', '.php', '.swift', '.kt', '.ts', '.json', '.xml',
            '.yaml', '.yml', '.sql', '.sh', '.bash', '.zsh', '.ini', '.md'
        }
    if exclude_extensions is None:
        exclude_extensions = {
            '.pyc', '.pyo', '.class', '.o', '.exe', '.dll', '.so', '.dylib'
        }

    file_tree = ""
    indent = "    " * level

    try:
        with os.scandir(directory) as it:
            for entry in sorted(it, key=lambda e: e.name.lower()):
                if entry.is_dir():
                    # Skip ignored directories
                    if entry.name in IGNORE_DIRS:
                        continue
                    file_tree += f"{indent}[{entry.name}]/\n"
                    file_tree += generate_file_tree(entry.path, level + 1, code_extensions, exclude_extensions)
                else:
                    _, ext = os.path.splitext(entry.name)
                    ext = ext.lower()
                    
                    # Skip excluded file types
                    if ext in exclude_extensions:
                        continue

                    file_tree += f"{indent}{entry.name}\n"

                    # If the file is a code file, include its contents
                    if ext in code_extensions:
                        try:
                            with open(entry.path, 'r', encoding='utf-8') as f:
                                content = f.read()
                            
                            # Prepare the content with proper indentation
                            content_lines = content.splitlines()
                            indented_content = '\n'.join([f"{indent}    {line}" for line in content_lines])
                            
                            # Append the content to the file tree
                            file_tree += f"{indent}    --- Start of {entry.name} ---\n"
                            file_tree += f"{indented_content}\n"
                            file_tree += f"{indent}    --- End of {entry.name} ---\n"
                        except Exception as e:
                            file_tree += f"{indent}    [Could not read file: {e}]\n"
    except PermissionError as pe:
        file_tree += f"{indent}[Permission Denied: {pe}]\n"
    except Exception as e:
        file_tree += f"{indent}[Error: {e}]\n"

    return file_tree

def create_file_tree_txt(directory):
    """
    Creates a 'file_tree_with_code_contents.txt' in the specified directory containing the file tree
    and contents of code files.

    Args:
        directory (str): The directory path where the file tree will be created.
    """
    print(f"Generating file tree for directory: {directory}")
    file_tree = generate_file_tree(directory)
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