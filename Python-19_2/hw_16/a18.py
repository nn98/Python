def transNumberA(a, alpha) :
    list = []
    for i in a :
        if i == " " : list.append(" ")
        else : list.append(alpha.index(i))

    return list

def transNumberCode(a, code, alpha) :
    list = []
    for i in range(len(a)) :
        list.append(alpha.index(code[i % len(code)]))

    return list

def decA(la, lcode, alpha) :
    an = ""
    for i in range(len(la)) :
        if la[i] == " " :
            an += " "
        else :
            if la[i]>= lcode[i] :
                an += alpha[la[i]- lcode[i]-1]
            else:
                an += alpha[25 + (la[i] - lcode[i])]

    return an

a = input()
code = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

la = transNumberA(a, alpha)
lcode = transNumberCode(a, code, alpha)

print(decA(la, lcode, alpha))