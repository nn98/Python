word = input()
key = input()

result = list(range(len(word)))
key_list = list(range(len(key)))

for i in range(len(key)):
    key_list[i]=ord(key[i])-ord('a')+1

for i in range(len(word)):
    if(word[i]==' '):
        result[i]=' '
        continue
    result[i]=ord(word[i])-ord('a')-key_list[i%len(key)]
    if(result[i]<0):
        result[i] = chr(result[i]+ord('a')+26)
    else:
        result[i] = chr(result[i]+ord('a'))
print(''.join(result))