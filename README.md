# URL Scheme Remover

This script is designed to remove "https://" and "http://" from domains and subdomains in a text file. This can be particularly useful for preprocessing URLs for tasks such as Nmap scanning, where the scheme is not required.

## Description

The script reads a file containing URLs, removes the "https://" and "http://" schemes, and writes the modified URLs to an output file. This helps in cleaning up URLs, making them ready for further processing with tools like Nmap.

## Usage

```
python3 remove.py input.txt
```
