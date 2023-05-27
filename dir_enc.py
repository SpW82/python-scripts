from cryptography.fernet import Fernet
import os

def lock(key, path):
    """
    Encrypting all files contained in target directory.
    Use file_dec to decrypted files.
    The same key is hardcoded in both file_enc and file_dec but can be user defined by uncommenting lines 33 & 34.
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
            enc_conts = Fernet(key).encrypt(conts)
        with open(file, 'wb') as f:
            f.write(enc_conts)
            print(f"[+] Encrypted : {f.name}")


def main():
    k = b'DKxZmlu4ExSeJUGfFRSMKUOl0QCpgGKM2cV_KAPt3_8='
    # k = input("[*] Enter key(decoded): ")
    # k = k.encode()
    p = input("[*] Enter path: ")
    lock(k, p)

if __name__ == '__main__':
    main()
