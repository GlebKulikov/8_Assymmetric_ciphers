import socket

import shifr


def read_key_file(path):
    with open(path, "r") as key_file:
        key = int(key_file.read())
    return key


def main():
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9091))
    pbckey = read_key_file("pbc.txt")
    pbskey = read_key_file("pbs.txt")
    prskey = read_key_file("prs.txt")
    sock.send(str(pbckey).encode())
    got = sock.recv(1024 * 8).decode()
    if got != "Ваш ключ не сертифицирован":
        port = int(got)
        sock.close()
        sock = socket.socket()
        sock.connect(("127.0.0.1", port))
    else:
        return

    while True:
        got = shifr.get_decrypted_message(sock, pbskey, prskey)
        print(got, end="")
        if "Вы вошли" in got:
            break
        print()
        sent = input('>')
        shifr.send_encrypted_message(sock, sent, prskey, pbckey)

    while True:
        sent = input()
        shifr.send_encrypted_message(sock, sent, prskey, pbckey)

        if sent == "exit":
            break

        got = shifr.get_decrypted_message(sock, pbskey, prskey)
        print(got, end="")

        got = shifr.get_decrypted_message(sock, pbskey, prskey)
        print(got, end="")
    sock.close()


if __name__ == '__main__':
    main()
