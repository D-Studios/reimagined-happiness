from bcrypt import *
from nltk.corpus import words
import nltk
import time


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

    # nltk.download('words')
    # print(words.words())

    # word_list = words.words()

    # filtered_words = [word for word in word_list if 6<=len(words)<=10]


    with open("en.txt", "r") as file:
    	word_list = file.readlines()

    filtered_words = [word[0:len(word)-1] for word in word_list if 6 <= len(word) <= 10]

    print(filtered_words)

    for word in filtered_words:
    	print(word)
    shadow = ""
    users = []
    forHashPws = []
    algorithms = []
    workFactors = []
    salts = []
    hashes = []


    with open("shadow.txt", "r") as file:
    	shadow = file.readlines()
    for j in range(0, len(shadow)):
	    shadow_split = shadow[j].split('$')
	    shadow_split2 = shadow[j].split(":")
	    user = shadow_split2[0]
	    forHashPw = shadow_split2[1]
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
	    print("forHashPws : ", forHashPw)
	    print("algorithm : ", algorithm)
	    print("workFactor : ", workFactor)
	    print("salt: ", salt)
	    print("hash: ", hashValue)
	    users.append(user)
	    forHashPws.append(forHashPw)
	    algorithms.append(algorithm)
	    workFactors.append(workFactor)
	    salts.append(salt)
	    hashes.append(hashValue)

    print(users)
    print(forHashPws)
    print(algorithms)
    print(workFactors)
    print(salts)
    print(hashes)

main()
