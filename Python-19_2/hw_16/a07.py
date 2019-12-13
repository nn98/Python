class Passw:
    def __init__(self,c,ke):
        self.c = c
        self.k = ke
    def password(self,c,key):
        if c == ' ':
         return c
        c = ord(c)
        for i in range(ord(key)- ord('a')+1):
            c -= 1
            if c == ord('a') -1:
                c = ord('z')
        return chr(c)

text = input()
key = input()
list = Passw(text,key)
psw = ""
j = 0
for i in text:
    psw += list.password(i,key[j])
    j += 1
    if j == len(key):
        j = 0
print(psw)