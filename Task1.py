import hashlib

def hash_input(input_string):
    # Create a SHA256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the input string (encoded to bytes)
    sha256_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal digest of the hash
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter the text to hash: ")
    
    # Hash the input and print the result
    hashed_value = hash_input(user_input)
    print(f"SHA256 Hash: {hashed_value}")
