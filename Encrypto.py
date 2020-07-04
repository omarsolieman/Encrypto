from cryptography.fernet import Fernet

print(r"""
                     ___________                                   __          
                     \_   _____/ ____   ___________ ___.__._______/  |_  ____  
                      |    __)_ /    \_/ ___\_  __ <   |  |\____ \   __\/  _ \ 
                      |        \   |  \  \___|  | \/\___  ||  |_> >  | (  <_> )
                     /_______  /___|  /\___  >__|   / ____||   __/|__|  \____/ 
                             \/     \/     \/       \/     |__|                
""")
print("Hello I am Encrypto your all in one encryption and decryption companion")


def encryption():
    print("Please make sure you have placed the text that you want to encrypt in 'text.txt' ")
    print("if content is already present it will be encrypted automatically ")
    file = open('key.key', 'rb')
    key = file.read()
    file.close()

    with open('text.txt', 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open('text.txt.encrypted', 'wb') as f:
        f.write(encrypted)


def decryption():
    print("Please place key in 'key.key' (No action is needed if Encrypto has been used to encrypt the content too)")
    print("Decrypting....")
    print("Decrypted Content will be in the file 'text.txt.decrypted' ")
    file = open('key.key', 'rb')
    key = file.read()
    file.close()

    with open('text.txt.encrypted', 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open('text.txt.decrypted', 'wb') as f:
        f.write(decrypted)


def keygeneration():
    print("key is generated")
    print("Key is in 'key.key'")
    key = Fernet.generate_key()
    print(key)

    file = open('key.key', 'wb')
    file.write(key)
    file.close()


keyGenerate = int(1)
decryptString = int(2)
encryptString = int(3)
Help = int(4)

while True:
    print("What should i do?")
    print("[1]Generate key")
    print("[2]Encrypt")
    print("[3]Decrypt")
    print("[4]Help")
    action = int(input(""))
    if action == keyGenerate:
        keygeneration()
    elif action == decryptString:
        encryption()
    elif action == encryptString:
        decryption()
    elif action == Help:
        print("This Section is still under development")
        print("Please Keep in mind that this app is still in beta stage")
    else:
        print("I'm Sorry that doesn't seem like a valid action")
