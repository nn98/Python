p = input()
k = input()

k = k * (len(p) // len(k) +1)


for i in range(len(p)):
    if ord(p[i]) == 32:
        key = " "
        print(key, end="")
    else:
        if ord(p[i]) > ord(k[i]):
            key = chr(ord(p[i]) - (ord(k[i])-96))
            print(key, end="")

        elif ord(p[i]) <= ord(k[i]):
            key = chr(122-(ord(k[i])-ord(p[i])+1)+1)
            print(key, end="")
