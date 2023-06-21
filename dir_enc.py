#!/usr/bin/python

import optparse
import os
from cryptography.fernet import Fernet

def lock(key, path):
    """
    Encrypting all files contained in target directory.
    Use file_dec to decrypted files.
    The same key is hardcoded in both dir_enc_parser and
    dir_dec_parser but can be, and should be, changed usging the -p or --pth flag.
    ENSURE the correct path is entered.
    """

    print(f'[*] Path : {path} ')
    os.chdir(path)
    dirs = []
    files = []

    for c in os.listdir():
        if os.path.isfile(c):
            print(f'[*] File: {c}')
            files.append(c)
        else:
            print(f'[*] Directory : {c} ')
            dirs.append(c)

    for file in files:
        with open(file, 'rb') as f:
            conts = f.read()
            enc_conts = Fernet(key).encrypt(conts)
        with open(file, 'wb') as f:
            f.write(enc_conts)
            print(f"[+] Encrypted : {f.name}")


def main():

    parser = optparse.OptionParser("Script to encrypt a target directory")
    parser.add_option('-p', '--pth', dest='pth', type='str', help='Absolute path of directory to encrypt')
    parser.add_option('-k', '--key', dest='key', type='str', help='Fernet key, not encoded')
    (options, args) = parser.parse_args()

    k = 'DKxZmlu4ExSeJUGfFRSMKUOl0QCpgGKM2cV_KAPt3_8='
    p = ''

    if options.pth is None:
        print(f'{parser.usage}\nFor encryption enter absolute path of directory to continue')
        exit(0)
    else:
        p = options.pth

    if options.key is None:
        pass
    else:
        k = options.key

    k = k.encode()
    lock(k, p)

if __name__ == '__main__':
    main()

