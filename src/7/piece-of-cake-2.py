def rot(text, amount):
    return chr((ord(text) + amount) % 128)


def find_rot_for_char(char1, char2):
    for i in range(0, 128):
        if rot(char1, i) == char2:
            print(f"{char1} needs {i} rotations to become {char2} or {i-128}")
            break
    else:
        print(f"{char1} no rotations found")



enc="he876:|I94kcxk6uohyp9t4cn}ti:vtcir7foowg8tbk8sfy~4166~"
known="he2024{"

for i, j in zip(known, enc):
    find_rot_for_char(i, j)

find_rot_for_char("}", "~")

def decrypt():
    encrypted = "he876:|I94kcxk6uohyp9t4cn}ti:vtcir7foowg8tbk8sfy~4166~"

    flag=""
    for (enc_char, amount) in zip(encrypted, "00674612947443578958611408777414804710387714755756388118445082180751150269761415002213210142"):
        flag += rot(enc_char, -int(amount))

    print(flag)


decrypt()

