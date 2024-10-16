from bcrypt import *
import bcrypt
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
    print(len(filtered_words))

    shadow = ""
    users = []
    forHashPws = []
    algorithms = []
    workFactors = []
    salts = []
    hashes = []
    hashDict = {}


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
	    for i in range(22, len(saltAndHash)-1):
	    	hashValue+=saltAndHash[i]
	    print("User : ", user)
	    print("forHashPws : ", forHashPw)
	    print("algorithm : ", algorithm)
	    print("workFactor : ", workFactor)
	    print("salt: ", salt)
	    print("hash: ", hashValue)
	    users.append(user)
	    forHashPws.append(forHashPw.encode('utf-8'))
	    algorithms.append(algorithm)
	    workFactors.append(workFactor)
	    salts.append(salt)
	    hashes.append(hashValue)
	    hashDict[user] = forHashPw.encode('utf-8')


    print(users)
    print(forHashPws)
    print(hashDict)

    howMany = 1

    print("\n\n\n\n")
    print("--------------------")
    currentPerson = 0
    for user, hash_value in hashDict.items():
	    start_time = time.time()    
	    for word in filtered_words :
	    	print(word)
	    	wordBytes = word.encode('utf-8')
	    	hashed_word = bcrypt.hashpw(wordBytes, hash_value[0:29])
	    	if bcrypt.checkpw(hashed_word, hash_value):
	    		elapsed_time = time.time() - start_time
	    		print(f"User: {user}, Password: {word}, Time taken: {elapsed_time:.4f} seconds (checkpw)")
	    		break
	    print("--------------------")
	    currentPerson += 1
	    if currentPerson >= howMany:
	    	break



main()
