def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, World\n")
            file.write("5674\n")
            file.write("Welcome!\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating the file: {e}")
    else:
        print("File created successfully.")
    finally:
        file.close()


def read_and_display():
    try:
        with open("my_file.txt", 'r') as file:
            print("Content of my_file.txt:")
            print(file.read())
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        file.close()


def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appended line.\n")
            file.write("54321\n")
            file.write("See you again\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to the file: {e}")
    else:
        print("Content appended to the file successfully.")
    finally:
        file.close()


if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()