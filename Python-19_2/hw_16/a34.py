sen = list(input())
key = list(input())
cipher = ""
while len(key) < len(sen):
    key += key
alp = "a b c d e f g j i j k l m n o p q r s t u v w x y z".split()
for i in range(len(key)):
    for j in range(26):
        if key[i] == alp[j]:
            key[i] = j + 1
        if sen[i] == alp[j]:
            sen[i] = j + 1
for m in range(len(key)):
    if sen[m] != " ":
        sen[m] -= key[m]
        if sen[m] <= 0:
            sen[m] += 26
for n in range(len(sen)):
    if sen[n] != " ":
        sen[n] = alp[sen[n]-1]
    cipher += sen[n]
print(cipher)