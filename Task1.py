import hashlib
import random
import time
import matplotlib.pyplot as plt

#Code returns SHA 256 output (with it truncated based on bit size)
def sha256_truncated(input_string, bit_size):
    full_hash = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    #Removes 0b from the beginning that is what [2:] is for
    binary_hash = bin(int(full_hash, 16))[2:].zfill(256)  
    return binary_hash[:bit_size]

#Code finds collision and returns the two messages whose hash collides, the collided hash, how many inputs had to be brute forced before found, and time elapsed.
def find_collision(bit_size):
    #Dictionary used (Birthday problem approach)
    hash_table = {}
    input_count = 0
    
    start_time = time.time()
    
    while True:
        #Create random string with 10 characters
        input_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))  
        #Get its hash
        truncated_hash = sha256_truncated(input_string, bit_size)
        
        #If hash already exists in dictionary and messages are different, return the messages, hash, inputs went through, and time elapsed
        if truncated_hash in hash_table:
            m0 = hash_table[truncated_hash]
            m1 = input_string
            if m0 != m1:
                end_time = time.time()
                return m0, m1, truncated_hash, input_count, end_time - start_time
        #Otherwise, add this hash and message to dictionary. Increment input went through by 1.
        else:
            hash_table[truncated_hash] = input_string
            input_count += 1

#Function to plot graph
def run_experiment():
    #Digests are multiples of 2 bits from 8 to 50 inclusive. This is list of all bit sizes.
    bit_sizes = range(8, 51, 2) 
    times = []
    input_counts = []
    
    #Loop through all bit sizes, finding collision for each and storing the input counts and times for graphing purposes.
    for bit_size in bit_sizes:
        print(f"Searching for collision with {bit_size}-bit truncated hash...")
        m0, m1, truncated_hash, input_count, elapsed_time = find_collision(bit_size)
        
        print(f"Collision found for {bit_size} bits:")
        print(f"m0 = {m0}, m1 = {m1}")
        print(f"Truncated hash = {truncated_hash}")
        print(f"Inputs checked = {input_count}")
        print(f"Time taken = {elapsed_time} seconds\n")
        
        times.append(elapsed_time)
        input_counts.append(input_count)
    
    #12 inch by 6 inch graph
    plt.figure(figsize=(12, 6))
    
    #1 row, 2 columns, left
    plt.subplot(1, 2, 1)
    #Times vs Digest
    plt.plot(bit_sizes, times, marker='o')
    plt.title('Collision Time vs Digest Size')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Time (seconds)')
    
    #1 row, 2 columns, rigth
    plt.subplot(1, 2, 2)
    #Number of inputs vs digest
    plt.plot(bit_sizes, input_counts, marker='o')
    plt.title('Number of Inputs vs Digest Size')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Number of Inputs')
    
    #Adjust spacing between subplot
    plt.tight_layout()

    #Show graphs
    plt.show()

if __name__ == "__main__":
    run_experiment()