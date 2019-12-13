def secret_code(a, b):
    if(ord(a) == 32):
        return chr(32)
    a1, b1 = ord(a)-96, ord(b)-96
    c = a1-b1 
    c += 26
    c = c%26
    if(c == 0):
        c = 26
    return chr(96+c)

clear = input()
password = input()
list = []

cl = len(clear)
pl = len(password)
for i in range(cl):
    list.append(secret_code(clear[i], password[i%pl]))
for i in range(cl):
    print(list[i], end='')