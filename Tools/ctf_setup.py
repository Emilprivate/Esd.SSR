import os
import json
import pyperclip

CONFIG_FILE = os.path.expanduser("~/.ctf_setup_config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def get_ctfs_directory():
    config = load_config()
    ctfs_dir = config.get('ctfs_directory')

    if ctfs_dir:
        change = input(f"Current Ctfs directory is '{ctfs_dir}'. Would you like to change it? (y/n): ").strip().lower()
        if change == 'n':
            return ctfs_dir

    ctfs_dir = input("Enter the path to your 'Ctfs' directory: ").strip()
    ctfs_dir = os.path.expanduser(ctfs_dir)  # Expand ~ to the full path

    if not os.path.isdir(ctfs_dir):
        print("Invalid path. Please provide a valid 'Ctfs' directory path.")
        return get_ctfs_directory()

    config['ctfs_directory'] = ctfs_dir
    save_config(config)
    return ctfs_dir

def get_existing_subdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def create_ctf_structure():
    current_dir = os.getcwd()
    path_parts = current_dir.split(os.sep)
    relative_path = []

    if 'Ctfs' in path_parts:
        ctfs_index = path_parts.index('Ctfs')
        base_path = os.sep.join(path_parts[:ctfs_index + 1])
        relative_path = path_parts[ctfs_index + 1:]

        if len(relative_path) >= 1:
            author = relative_path[0]
        else:
            author = None
    else:
        base_path = get_ctfs_directory()
        author = None

    if not author:
        existing_authors = get_existing_subdirs(base_path)
        if existing_authors:
            print("Existing authors:")
            for i, auth in enumerate(existing_authors, start=1):
                print(f"{i}) {auth}")
                
            author_choice = input("Select CTF author by number or type a new author name: ").strip()
            if author_choice.isdigit():
                author_index = int(author_choice) - 1
                if 0 <= author_index < len(existing_authors):
                    author = existing_authors[author_index]
                else:
                    print("Invalid number, please provide a valid number.")
                    return
            else:
                author = author_choice
        else:
            author = input("No existing authors found. Enter the CTF author name: ").strip()

    author_path = os.path.join(base_path, author)
    os.makedirs(author_path, exist_ok=True)

    if len(relative_path) > 1:
        category = relative_path[1]
    else:
        existing_categories = get_existing_subdirs(author_path)
        if existing_categories:
            print("Existing categories:")
            for i, cat in enumerate(existing_categories, start=1):
                print(f"{i}) {cat}")

            category_choice = input("Select CTF category by number or type a new category name: ").strip()
            if category_choice.isdigit():
                category_index = int(category_choice) - 1
                if 0 <= category_index < len(existing_categories):
                    category = existing_categories[category_index]
                else:
                    print("Invalid number, please provide a valid number.")
                    return
            else:
                category = category_choice
        else:
            category = input("No existing categories found. Enter the CTF category: ").strip()

    category_path = os.path.join(author_path, category)
    os.makedirs(category_path, exist_ok=True)

    challenge_name = input("Enter the CTF challenge name: ").strip()
    challenge_path = os.path.join(category_path, challenge_name)
    os.makedirs(challenge_path, exist_ok=True)

    workfolder_path = os.path.join(challenge_path, 'workfolder')
    os.makedirs(workfolder_path, exist_ok=True)

    readme_path = os.path.join(challenge_path, 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write(f"# Writeup for {author} : {challenge_name}\n")
        readme_file.write("## Steps:\n")
        readme_file.write("## Flag:\n")
        readme_file.write("``` ```\n")

    cd_command = f"cd '{challenge_path}'"
    pyperclip.copy(cd_command)
    print(f"CTF structure created successfully at {challenge_path}")
    print(f"The command to navigate to the challenge directory has been copied to your clipboard: {cd_command}")

if __name__ == "__main__":
    create_ctf_structure()

