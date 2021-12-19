import random

certs = "certs.txt"
paths = ['pbc.txt', 'pbs.txt', 'prc.txt', 'prs.txt']


def calculate_key(b, p, r):
    return b ** p % r


def add_keys(keys):
    for i in range(4):
        with open(paths[i], 'w') as key_file:
            key_file.write(str(keys[i]))
    with open(certs, 'a') as key_file:
        key_file.write(f"{keys[0]}:{keys[2]}\n")


def main():
    a = random.randint(0, 100)
    g = random.randint(0, 10000)
    p = random.randint(0, 10000)
    pbckey = calculate_key(g, a, p)
    b = random.randint(0, 100)
    pbskey = calculate_key(g, b, p)
    prckey = calculate_key(pbskey, a, p)
    prskey = calculate_key(pbckey, b, p)
    add_keys([pbckey, pbskey, prckey, prskey])


if __name__ == '__main__':
    main()
