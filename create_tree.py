import os
import sys

# List of directories and files to ignore
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

IGNORE_FILES = {
    'create_tree.py',
    'file_tree.txt',
    'create_tree_and_get_contents.py',
    'file_tree_with_code_contents.txt',
    'create_tree_and_get_contents.exe',
    'create_tree.exe'
}

def generate_file_tree(directory, prefix=""):
    file_tree = ""
    entries = list(os.scandir(directory))
    entries = [
        entry for entry in entries
        if entry.name not in IGNORE_DIRS and entry.name not in IGNORE_FILES
    ]
    entry_count = len(entries)
    
    for i, entry in enumerate(entries):
        connector = "├── " if i < entry_count - 1 else "└── "
        
        if entry.is_dir():
            file_tree += f"{prefix}{connector}[{entry.name}]/\n"
            extension = "│   " if i < entry_count - 1 else "    "
            file_tree += generate_file_tree(entry.path, prefix + extension)
        else:
            file_tree += f"{prefix}{connector}{entry.name}\n"
    
    return file_tree

def create_file_tree_txt(directory):
    file_tree = generate_file_tree(directory)
    file_name = os.path.join(directory, "file_tree.txt")
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(file_tree)

if __name__ == "__main__":
    # Determine the directory where the .exe or .py file is located
    if getattr(sys, 'frozen', False):
        current_directory = os.path.dirname(sys.executable)  # For .exe
    else:
        current_directory = os.path.dirname(os.path.abspath(__file__))  # For regular .py execution
    
    # Dynamically add this script's filename to the ignore list
    script_name = os.path.basename(__file__)
    IGNORE_FILES.add(script_name)
    
    create_file_tree_txt(current_directory)
    print(f"File tree created and saved as 'file_tree.txt' in {current_directory}")