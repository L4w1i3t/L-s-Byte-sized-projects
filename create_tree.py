import os
import sys

def generate_file_tree(directory, level=0):
    file_tree = ""
    indent = "    " * level
    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_dir():
                file_tree += f"{indent}[{entry.name}]/\n"
                file_tree += generate_file_tree(entry.path, level + 1)
            else:
                file_tree += f"{indent}{entry.name}\n"
    return file_tree

def create_file_tree_txt(directory):
    file_tree = generate_file_tree(directory)
    file_name = os.path.join(directory, "file_tree.txt")
    with open(file_name, "w") as file:
        file.write(file_tree)

if __name__ == "__main__":
    # Determine the directory where the .exe or .py file is located
    if getattr(sys, 'frozen', False):
        current_directory = os.path.dirname(sys.executable)  # For PyInstaller .exe
    else:
        current_directory = os.path.dirname(os.path.abspath(__file__))  # For regular .py execution

    create_file_tree_txt(current_directory)
    print(f"File tree created and saved as 'file_tree.txt' in {current_directory}")
