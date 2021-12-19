def send_encrypted_message(conn, message, prkey, pbkey):
    print("•" * 20)
    message = str(message)
    print("\n" + message)
    message = encrypt(prkey, message)
    message = encrypt(pbkey, message)
    print("   |")
    print("   V")
    print(message + "\n")
    print("•" * 20)
    conn.send(message.encode())


def get_decrypted_message(conn, pbkey, prkey):
    message = conn.recv(1024).decode()
    print("•" * 20)
    print("\n" + message)
    message = decrypt(pbkey, message)
    message = decrypt(prkey, message)
    print("   |")
    print("   V")
    print(message + "\n")
    print("•" * 20)
    return message


def encrypt(key, string):
    res = ''
    for char in string:
        res += chr(ord(char) ^ key)
    return res


def decrypt(k, msg):
    return encrypt(k, msg)
