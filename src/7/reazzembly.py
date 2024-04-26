leet_1 = 1
leet_2 = 13
leet_3 = 133
leet_4 = 1337
enc_flag = input("enter the encrypted flag")

l = list(enc_flag)
for i in range(len(l)):
    l[i] = chr(ord(l[i]) ^ (i % (leet_1 % 10)))
for i in range(len(l) // 2, len(l)):
    l[i] = chr(ord(l[i]) + leet_2 % 10)
for i in range(len(l) // 2):
    l[i] = chr(ord(l[i]) - leet_3 % 10)
for i in range(len(l)):
    l[i] = chr(ord(l[i]) + leet_4 % 10)
print("".join(l))
