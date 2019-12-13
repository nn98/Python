p = input("")
p = p.lower()
a = input("")
a = a.lower()
r1 = ''
for i in range(len(p)):
    if p[i] != " ":
        p1 = ord(p[i])
        a1 = ord(a[i % len(a)])
        if p1 - a1 < 1:
            p1 = ord('z') - (a1 - p1)
            r1 += chr(p1)
        else:
            p1 = 96 + (p1 - a1)
            r1 += chr(p1)
    else:
        r1 += p[i]
print(r1)
