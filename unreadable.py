from cryptography.fernet import Fernet
import os

"""
This script is to aid the process of making a directories files unreadable.
If deleting sensitive files, run this program on a directory containing said files prior to deleting.
ENSURE the correct path is entered as all file contained within the target directory will be encrypted and 
non_recoverable as the key is not saved and deleted from memory when the program ends essentially destroying the files.
"""

def lock(key, path):
    os.chdir(path)
    dirs = []
    files = []

    for c in os.listdir():
        if os.path.isfile(c):
            files.append(c)
        else:
            dirs.append(c)

    for file in files:
        with open(file, 'rb') as f:
            conts = f.read()
            enc_conts = Fernet(key).encrypt(conts)
        with open(file, 'wb') as f:
            f.write(enc_conts)
            print(f"[+] Encrypted : {f.name}")

def main():
    k = Fernet.generate_key()
    p = input("[*] Enter path: ")
    lock(k, p)

if __name__ == '__main__':
    main()
