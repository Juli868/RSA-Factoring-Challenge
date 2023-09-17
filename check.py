#!/usr/bin/python3
import sys
import os
from prime_generatr import generator
prime_number = [2]

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
            a = 3
            generate = generator(a)
            if generate == 1:
                prime_number.append(a)
                a += 1
                continue
            else:
                a += 1
