import os
import shutil


def create_file(file_path, content=""):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' created successfully.")


def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return "File not found."


def update_file(file_path, content):
    if os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(content)
        print(f"File '{file_path}' updated successfully.")
    else:
        print("File not found.")


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    else:
        print("File not found.")


def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory '{dir_path}' created successfully.")


def delete_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        print(f"Directory '{dir_path}' deleted successfully.")
    else:
        print("Directory not found.")


def list_contents(path):
    if os.path.exists(path):
        return os.listdir(path)
    else:
        return "Path not found."


if __name__ == "__main__":
    while True:
        print("\nFile Management System")
        print("1. Create File")
        print("2. Read File")
        print("3. Update File")
        print("4. Delete File")
        print("5. Create Directory")
        print("6. Delete Directory")
        print("7. List Contents")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter file path: ")
            content = input("Enter file content (optional): ")
            create_file(path, content)
        elif choice == "2":
            path = input("Enter file path: ")
            print(read_file(path))
        elif choice == "3":
            path = input("Enter file path: ")
            content = input("Enter content to append: ")
            update_file(path, content)
        elif choice == "4":
            path = input("Enter file path: ")
            delete_file(path)
        elif choice == "5":
            path = input("Enter directory path: ")
            create_directory(path)
        elif choice == "6":
            path = input("Enter directory path: ")
            delete_directory(path)
        elif choice == "7":
            path = input("Enter directory path: ")
            print(list_contents(path))
        elif choice == "8":
            break
        else:
            print("Invalid choice, please try again.")
