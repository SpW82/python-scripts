from cryptography.fernet import Fernet
import os

def unlock(key, path):

    """
    Decrypting all files contained in target directory.
    The same key is hardcoded in both file_enc and file_dec but can be made user defined by uncommenting lines 33 & 34.
    ENSURE the correct path is entered.
    """

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
            dec_conts = Fernet(key).decrypt(conts)
        with open(file, 'wb') as f:
            f.write(dec_conts)
            print(f"[+] Decrypted : {f.name}")

def main():

    k = b'DKxZmlu4ExSeJUGfFRSMKUOl0QCpgGKM2cV_KAPt3_8='
    # k = input("[*] Enter key(decoded): ")
    # k = k.encode()
    p = input("[*] Enter path: ")
    unlock(k, p)


if __name__ == '__main__':
    main()
