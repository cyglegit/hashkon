import sys
import hashlib

def calculate_hashes(file_path):
    hashes = {}
    try:
        # Open the file in binary mode
        with open(file_path, "rb") as file:
            data = file.read()
            # Calculate MD5 hash
            md5_hash = hashlib.md5(data).hexdigest()
            # Calculate SHA-1 hash
            sha1_hash = hashlib.sha1(data).hexdigest()
            # Calculate SHA-256 hash
            sha256_hash = hashlib.sha256(data).hexdigest()
            # Store hashes in a dictionary
            hashes['MD5'] = md5_hash
            hashes['SHA-1'] = sha1_hash
            hashes['SHA-256'] = sha256_hash
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied to access the file!")
    except Exception as e:
        print("An error occurred:", e)
    return hashes

def show_usage():
    print('\n')
    print("Usage: python script.py <file-address>")
    print("Calculates MD5, SHA-1, and SHA-256 hashes of the specified file.")

if __name__ == "__main__":
    # Check if the file address is provided as command line argument
    if len(sys.argv) == 1:  # If no command line arguments are provided
        show_usage()
        sys.exit(0)
    elif len(sys.argv) != 2:
        print("Invalid number of arguments!")
        show_usage()
        sys.exit(1)
    
    file_path = sys.argv[1]  # Get file address from command line argument
    try:
        hashes = calculate_hashes(file_path)
        print('\n')
        print("MD5 Hash:", hashes['MD5'])
        print("SHA-1 Hash:", hashes['SHA-1'])
        print("SHA-256 Hash:", hashes['SHA-256'])
    except Exception as e:
        print("An error occurred:", e)
