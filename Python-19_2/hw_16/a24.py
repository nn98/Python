fstr = input()
sstr = input()
k = len(fstr)//len(sstr)+1
sstr = sstr*k
key_word=[]
for i in range(len(fstr)):
    key_word.append(' ')
    if ord(fstr[i]) == 32:
        key_word[i] = ' '
    else:
        if ord(fstr[i]) - ord(sstr[i]) > 0:
            key_word[i] = chr(ord(fstr[i]) - ord(sstr[i]) + 96)
        else:
            key_word[i] = chr(ord(fstr[i]) - ord(sstr[i]) + 122)
key_word = ''.join(key_word)
print(key_word)
