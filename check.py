#!/usr/bin/python3
import sys
import os
prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547]

check = []
if len(sys.argv) != 2:
    print("Usage: Program name your file")
    sys.exit(-1)
file_path = sys.argv[1]
current_directory = os.getcwd()
file_path = os.path.join(current_directory ,file_path)
try:
    with open(file_path, 'r') as file:
        for line in file:
            check.append(int(line.strip()))
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
for k in range(len(check)):
    for i in range(len(prime_number)):
        if (check[k] % prime_number[i] == 0):
            second = check[k] / prime_number[i]
            print(f"{check[k]}={second:.0f}*{prime_number[i]}")
            break
        else:
            continue
