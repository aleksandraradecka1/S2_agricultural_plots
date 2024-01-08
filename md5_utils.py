import hashlib
import re
import os

def extract_info(file_path):
    """
    Extracts two pieces of information from the input file
    :param file_path: str
        path to the file containing information 
    :return: tuple of str
        original md5 hash value and name of the file to be checked
    """
    try:
        with open(file_path, "r") as file:
            file_content = file.read().strip()
            parts = re.split(r'\s+', file_content)
            if len(parts) == 2 and len(parts[0]) == 32:
                return tuple(parts)
            else:
                print(f"There is something wrong with the content of the file '{file_path}'")
                return None
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found")
        return None

def find_file(file_name, start_directory):
    """
    Recursively searches for a file with a specific name in a given directory and its subdirectories
    :param file_name: str
        name of the file to be found
    :param start_directory: str
        directory where the search starts
    :return: str
        file path matching the given file name
    """
    result = []

    for root, dirs, files in os.walk(start_directory):
        if file_name in files:
            result.append(os.path.join(root, file_name))

    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print(f"More than one file of name '{file_name}' exists in '{start_directory}' directory")
        for path in result:
            print(path)
        return None
    else:
        print(f"There are no files of name '{file_name}' in '{start_directory}' directory")
        return None

def compute_md5hash(file_path, chunk_size=8192):
    """
    Computes the md5 hash value of the input file
    :param file_path: str
        path to the file to be checked
    :param chunk_size: int
        size of data chunks to read and hash at a time
    :return: str
        computed md5 hash value represented as a hexadecimal string
    """
    md5_hash = hashlib.md5()
    
    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                md5_hash.update(data)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found")
        return None

def compare_md5hashes(file_path, original_md5hash):
    """
    Checks if the md5 hash value computed for the input file is the same as its original md5 hash value
    :param file_path: str
        path to the file to be checked
    :param original_md5hash: str
        original md5 hash value of the input file
    """
    computed_md5hash = compute_md5hash(file_path)
    
    if computed_md5hash == original_md5hash:
        print("The computed and original md5 hash values are the same")
        print(f"The hash value is: '{original_md5hash}'")
    else: 
        print("The computed and original md5 hash values are not the same")
        print(f"The computed hash value is: '{computed_md5hash}'")
        print(f"The original hash value is: '{original_md5hash}'")