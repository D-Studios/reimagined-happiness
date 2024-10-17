import bcrypt

def main():
    print("Hello World")
    # example password 
    password = 'password123'
    
    # converting password to array of bytes 
    bytes = password.encode('utf-8') 
    
    # generating the salt 
    salt = bcrypt.gensalt() 
    
    # Hashing the password 
    hash = bcrypt.hashpw(bytes, salt) 
    
    print(hash)

if 'name' == "__main__":
    main()