w = input()
k = input()
j = 0

for i in range(0, len(w)):
    if (j == len(k)):
        j = 0
    if (w[i] == " "):
        print(w[i], end="")
        j += 1
        continue
    a = ord(w[i])
    b = ord(k[j])
    c = a - b
    if (c < 1):
        c += 26

    print(chr(c+96), end="")

    j += 1