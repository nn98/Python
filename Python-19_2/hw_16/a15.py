def Code (s, key_s):
    if s == ' ':
        return s
    s = ord(s)
    for _ in range(ord(key_s)-ord('a')+1):
        s -= 1
        if s == ord('a')-1:
            s = ord('z')
    return chr(s)

plain_text = input()
key = input()
key_len = len(key)
key_idx = 0
cryptogram = ''
for c in plain_text:
    cryptogram += Code(c, key[key_idx])
    key_idx += 1
    if key_idx == key_len:
        key_idx = 0
print(cryptogram)