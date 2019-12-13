def encrypt(c, key_c):
    if c == ' ':
        return c
    c = ord(c)
    for _ in range(ord(key_c)-ord('a')+1):
        c -=1
        if c == ord('a')-1:
            c = ord('z')
    return chr(c)

plain_text = input()
key = input()
key_len = len(key)
key_idx = 0
cipher_text = ''
for c in plain_text:
    cipher_text += encrypt(c, key[key_idx])
    key_idx += 1
    if key_idx == key_len:
        key_idx = 0
print(cipher_text)