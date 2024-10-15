import hashlib
import random
import time
import matplotlib.pyplot as plt

def sha256_truncated(input_string, bit_size):
    full_hash = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    binary_hash = bin(int(full_hash, 16))[2:].zfill(256)  
    return binary_hash[:bit_size]

def find_collision(bit_size):
    hash_table = {}
    input_count = 0
    
    start_time = time.time()
    
    while True:
        input_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))  
        truncated_hash = sha256_truncated(input_string, bit_size)
        
        if truncated_hash in hash_table:
            m0 = hash_table[truncated_hash]
            m1 = input_string
            if m0 != m1:
                end_time = time.time()
                return m0, m1, truncated_hash, input_count, end_time - start_time
        else:
            hash_table[truncated_hash] = input_string
            input_count += 1

def run_experiment():
    bit_sizes = range(8, 51, 2) 
    times = []
    input_counts = []
    
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
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(bit_sizes, times, marker='o')
    plt.title('Collision Time vs Digest Size')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Time (seconds)')
    
    plt.subplot(1, 2, 2)
    plt.plot(bit_sizes, input_counts, marker='o')
    plt.title('Number of Inputs vs Digest Size')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Number of Inputs')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_experiment()