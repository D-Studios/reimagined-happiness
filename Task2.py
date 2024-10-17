from bcrypt import *

def main():
    # print("Hello World")
    # # example password 
    # password = 'password123'
    
    # # converting password to array of bytes 
    # bytes = password.encode('utf-8') 
    
    # # generating the salt 
    # salt = bcrypt.gensalt() 
    
    # # Hashing the password 
    # hash = bcrypt.hashpw(bytes, salt) 
    
    # print(hash)

    shadow = ""

    with open("shadow.txt", "r") as file:
    	shadow = file.readlines()
    for j in range(0, len(shadow)):
	    shadow_split = shadow[j].split('$')
	    user = shadow_split[0]
	    algorithm = shadow_split[1]
	    workFactor = shadow_split[2]
	    saltAndHash = shadow_split[3]
	    salt = ""
	    hashValue = ""
	    for i in range(0, 22):
	    	salt+=saltAndHash[i]
	    for i in range(22, len(saltAndHash)):
	    	hashValue+=saltAndHash[i]
	    print("User : ", user)
	    print("algorithm : ", algorithm)
	    print("workFactor : ", workFactor)
	    print("salt: ", salt)
	    print("hash: ", hashValue)


main()