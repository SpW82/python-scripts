import os
from cryptography.fernet import Fernet

class Recursive(object):

    """
    Starting at a specified path, encrypting/decrypting all files contained in pwd then entering all
    contained directories and repeating.
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
        # print(f"[*] Directories : {dirs}")

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
                print(f"[!] path: {p}")
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
                print(f"[!] path: {p}")
                self.target_dec(p, k)


def main():
    # Encryption tests  -->>  Comment out decrypt first, run encrypt then reverse

    # To encrypt
    rec = Recursive()

    # Line 91  -->>  to generate a new key and save to a file
    t_k = Recursive.gen_key()
    p = input("[*] Enter path: ")
    rec.target_enc(p, t_k)

    # To decrypt
    # with open("k.key", "rb") as k:
    #     tk2 = k.read()
    #
    # p = input("[*] Enter path: ")
    # rec.target_dec(p, tk2)

if __name__ == '__main__':
    main()
