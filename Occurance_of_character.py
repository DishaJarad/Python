def count_a_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            count = text.count('a')
            print(f"Occurrences of 'a' in the file: {count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Provide the file path here
file_path = 'input.txt' 
count_a_occurrences(file_path)
