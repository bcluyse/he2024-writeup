reversed_file = None
file_in_bytes = []

with open("../files/gnp.galf", "rb") as f:
    while byte := f.read(1):
        file_in_bytes.append(byte)

    reversed_file = file_in_bytes[::-1]

with open("../files/egg_reverser_flag.png", "wb") as f:
    for byte in reversed_file:
        f.write(byte)
