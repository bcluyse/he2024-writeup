from random import *

# flag="REDACTED"
# cipher=[]
# kee=randint(1,10000)
# off=randint(1,5)
# for f in flag:
#     cipher.append(str((ord(f) - off) ^ kee))
#
# print(kee, off, cipher)

encrypted = ['6255', '6248', '6181', '6183', '6181', '6203', '6258', '6255', '6203', '6267', '6250', '6255', '6230', '6203', '6250', '6250', '6202', '6200', '6200', '6230', '6254', '6245', '6203', '6241', '6267', '6202', '6251', '6256']


def encrypt(value, kee, off):
    return str((ord(value) - off) ^ kee)


def decrypt(value, kee, off):
    return chr((int(value) ^ kee) + off)


encrypted_prefix = zip(encrypted[0:7], ["h", "e", "2", "0", "2", "4", "{"])
candidates_kee = list(range(1, 10000))
candidates_off = list(range(1, 5))

for (key, value) in encrypted_prefix:
    next_iteration_kee = []
    next_iteration_off = []

    for kee in candidates_kee:
        for off in candidates_off:
            if decrypt(key, kee, off) == value:
                next_iteration_kee.append(kee)
                next_iteration_off.append(off)

    candidates_kee = next_iteration_kee
    candidates_off = next_iteration_off
    print(candidates_kee, candidates_off)

print("Final candidates", candidates_kee, candidates_off)

if len(candidates_off) == len(candidates_kee) == 1:
    kee = candidates_kee[0]
    off = candidates_off[0]

    result = [decrypt(x, kee, off) for x in encrypted]
    print(f"Flag={''.join(result)}")
