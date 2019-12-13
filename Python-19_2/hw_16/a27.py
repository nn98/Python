def word(i, key_c):
    if i == ' ':
        return i
    i = ord(i)
    for _ in range(ord(key_c)-ord('a')+1):
        i -= 1
        if i == ord('a')-1:
            i = ord('z')
        return chr(i)

text = input()
key = input()
key_len = len(key)
key_idx = 0
come_text = ''

for c in text:
    come_text += word(c, key[key_idx])
    key_idx += 1
    if key_idx == key_len:
        key_idx = 0
        
print(come_text)