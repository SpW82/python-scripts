#!/usr/bin/python

import optparse
import os
from cryptography.fernet import Fernet

def lock(key, a_path):
    """
    Encrypts specified file.
    Use file_dec to decrypted files.
    The same key is hardcoded in both file_enc and file_dec but can be changed by using the -k or --key flag.
    ENSURE the correct path is entered.
    """

    dirs = a_path.split('/')
    t_file = dirs[-1]
    path = ''
    for d in dirs[:-1]:
        path = f"{path}/{d}"

    os.chdir(path)
    files = []

    for c in os.listdir():
        if os.path.isfile(c):
            files.append(c)
        else:
            pass

    for file in files:
        if file == t_file:
            with open(file, 'rb') as f:
                conts = f.read()
                enc_conts = Fernet(key).encrypt(conts)
            with open(file, 'wb') as f:
                f.write(enc_conts)
                print(f"[+] Encrypted : {f.name}")

def main():

    parser = optparse.OptionParser("Script to encrypt a target file")
    parser.add_option('-p', '--pth', dest='pth', type='str', help='Absolute path of file to encrypt')
    parser.add_option('-k', '--key', dest='key', type='str', help='Fernet key, not encoded')
    (options, args) = parser.parse_args()
    k = 'DKxZmlu4ExSeJUGfFRSMKUOl0QCpgGKM2cV_KAPt3_8='
    p = ''
    # print(f"[*] Options : {options.usage()}")
    if options.pth is None:
        print(f'{parser.usage}\nFor encryption enter absolute path of file to continue')
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
