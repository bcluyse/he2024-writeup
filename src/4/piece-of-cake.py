def rot(text, amount):
    return chr((ord(text) + amount) % 128)


def find_rot_for_char(char1, char2):
    for i in range(0, 128):
        if rot(char1, i) == char2:
            print(f"{char1} needs {i} rotations to become {char2}")
            break
    else:
        print(f"{char1} no rotations found")


def get_pi_iteration():
    return "1415926535897932384626433832795028841971693993751058209749445923"


def decrypt():
    encrypted = "ii35;6Ykf|h~j8adgf7ve5uuiw37wflaj}x`9rbgj|7"

    for char1, char2 in zip("he2024{", encrypted):
        find_rot_for_char(char1, char2)


    flag=""
    for (enc_char, amount) in zip(encrypted, get_pi_iteration()):
        flag+= rot(enc_char, -int(amount))

    print(flag)



decrypt()
