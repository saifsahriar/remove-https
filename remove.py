#! /usr/bin/python3

import sys
import re

if(len(sys.argv) < 2):
    print("[-] Insufficient parameters")
    print("[+] Usage: python3 remove.py <filename>")

filename = sys.argv[1]
output_file = "output.txt"

try:
    with open(filename, 'r') as file, open(output_file, 'w') as op_file:
        lines = file.readlines()
        pattern = re.compile(r'https?://')
        for line in lines:
            line = pattern.sub('', line)
            op_file.write(line)

except FileNotFoundError:
    print(f"{filename} not found")
    sys.exit(1)

