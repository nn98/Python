dec = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10,
       "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20,
       "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25}
enc = { }

for j in dec :
    val = dec[j]
    enc[val] = j

sentence = input()
code = input()
newSentence = ""
for i in range(len(sentence)) :
    if sentence[i].isalpha() :
        if dec[sentence[i]] - dec[code[i % len(code)]]  > 0:
            newSentence += (enc[dec[sentence[i]] - dec[code[i % len(code)]] - 1])
        elif sentence[i] == code[i % len(code)] :
            newSentence += "z"
        else :
            newSentence += (enc[25 - abs(dec[sentence[i]] - dec[code[i % len(code)]])])
    else :
        newSentence += " "

print(newSentence)