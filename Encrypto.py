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
    while True:
        keyinput = int(1)
        txt = int(2)
        print("How would you like to input the key?")
        print("[1] Input key here")
        print("[2] Use 'key.key'")
        actionenc = int(input(""))
        if actionenc == keyinput:
            keyinp = input("").encode()
            file = open('key.key', 'wb')
            file.write(keyinp)
            file.close()
            txtinput = int(1)
            txttxt = int(2)
            print("How would you like to input the key?")
            print("[1] Input text here")
            print("[2] Use 'text.txt'")
            actionencm = int(input(""))
            if actionencm == txtinput:
                txtinp = input("").encode()
                file = open('text.txt', 'wb')
                file.write(txtinp)
                file.close()
                file = open('key.key', 'rb')
                key = file.read()
                file.close()

                with open('text.txt', 'rb') as f:
                    data = f.read()

                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)

                with open('text.txt.encrypted', 'wb') as f:
                    f.write(encrypted)

                print("encrypted")

            elif actionencm == txttxt:
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

                print("encrypted")

            else:
                print("I'm Sorry that doesn't seem like a valid action")
                choices()
            choices()
        elif actionenc == txt:
            txtinput = int(1)
            txttxt = int(2)
            print("How would you like to input the key?")
            print("[1] Input text here")
            print("[2] Use 'text.txt'")
            actionencm = int(input(""))
            if actionencm == txtinput:
                txtinp = input("").encode()
                file = open('text.txt', 'wb')
                file.write(txtinp)
                file.close()
                file = open('key.key', 'rb')
                key = file.read()
                file.close()

                with open('text.txt', 'rb') as f:
                    data = f.read()

                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)

                with open('text.txt.encrypted', 'wb') as f:
                    f.write(encrypted)

                print("encrypted")

            elif actionencm == txttxt:
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

                print("encrypted")

            else:
                print("I'm Sorry that doesn't seem like a valid action")
                choices()
            choices()
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

            print("encrypted")
            
            choices()
        else:
            print("I'm Sorry that doesn't seem like a valid action")
            choices()


def decryption():
    keyinput = int(1)
    txt = int(2)
    print("How would you like to input the key?")
    print("[1] Input key here")
    print("[2] Use 'key.key'")
    actionenc = int(input(""))
    if actionenc == keyinput:
        keyinp = input("").encode()
        file = open('key.key', 'wb')
        file.write(keyinp)
        file.close()
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
    elif actionenc == txt:
        print(
            "Please place key in 'key.key' (No action is needed if Encrypto has been used to encrypt the content too)")
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
    else:
        print("I'm Sorry that doesn't seem like a valid action")
        choices()


def keygeneration():
    print("key is generated")
    print("Key is in 'key.key'")
    key = Fernet.generate_key()
    print(key)

    file = open('key.key', 'wb')
    file.write(key)
    file.close()


def choices():
    keygenerate = int(1)
    decryptstring = int(2)
    encryptstring = int(3)
    helpm = int(4)

    while True:
        print("What should i do?")
        print("[1]Generate key")
        print("[2]Encrypt")
        print("[3]Decrypt")
        print("[4]Help")
        action = int(input(""))
        if action == keygenerate:
            keygeneration()
        elif action == decryptstring:
            encryption()
        elif action == encryptstring:
            decryption()
        elif action == helpm:
            print("This Section is still under development")
            print("Please Keep in mind that this app is still in beta stage")
        else:
            print("I'm Sorry that doesn't seem like a valid action")


keygenerate = int(1)
decryptstring = int(2)
encryptstring = int(3)
helpm = int(4)

while True:
    print("What should i do?")
    print("[1]Generate key")
    print("[2]Encrypt")
    print("[3]Decrypt")
    print("[4]Help")
    action = int(input(""))
    if action == keygenerate:
        keygeneration()
    elif action == decryptstring:
        encryption()
    elif action == encryptstring:
        decryption()
    elif action == helpm:
        print("This Section is still under development")
        print("Please Keep in mind that this app is still in beta stage")
    else:
        print("I'm Sorry that doesn't seem like a valid action")
