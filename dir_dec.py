from cryptography.fernet import Fernet
import os
import optparse


def unlock(key, path):
    """
    Decrypting all files contained in target directory.
    The same key is hardcoded in both dir_enc_parser and
    dir_dec_parser but can be, and should be, changed usging the -p or --pth flag.
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
    parser = optparse.OptionParser("Script to decrypt a target directory")
    parser.add_option('-p', '--pth', dest='pth', type='str', help='Absolute path of directory to decrypt')
    parser.add_option('-k', '--key', dest='key', type='str', help='Fernet key, not encoded')
    (options, args) = parser.parse_args()

    k = 'DKxZmlu4ExSeJUGfFRSMKUOl0QCpgGKM2cV_KAPt3_8='
    p = ''

    if options.pth is None:
        print(f'{parser.usage}\nFor decryption enter absolute path of directory to continue')
        exit(0)
    else:
        p = options.pth

    if options.key is None:
        pass
    else:
        k = options.key

    k = k.encode()
    unlock(k, p)


if __name__ == '__main__':
    main()
