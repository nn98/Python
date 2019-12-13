def find(c, key_c):
    if c == ' ':
        return c
    c = ord(c)
    for _ in range(ord(key_c)-ord('a')+1):
        c -= 1
        if c == ord('a')-1:
            c = ord('z')
    return chr(c)

ntext = input()
key = input()
key_len = len(key)
key_idx = 0
text = ''
for c in ntext:
    text += find(c, key[key_idx])
    key_idx += 1
    if key_idx == key_len:
        key_idx = 0
print(text)