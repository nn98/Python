def cipher(str, keyindex):
    """
    Vigenere cipher 방법을 사용해 평문을 암호화하고, 암호문을 반환
    :param str: 평문
    :param keyindex: 암호화 키
    :return: 암호문
    """
    k = ord(keyindex) - ord('a')+1
    s = ord(str) - ord('a')+1
    if s>k:
        p = ord('a')+(s-k)-1
    else:
        p = ord('z')-(k-s)
    return chr(p)

def count_reset(c,l):
    """
    암호화키가 반복되도록 index를 1씩 증가시키고 index가 len(key)값이 되면 초기화
    :param c: 인덱스
    :param l: 암호화 키 길이
    :return: 인덱스
    """
    if c < l-1:
        c += 1
    else:
        c = 0
    return c

#프로그램 시작
str = input()   #평문 입력
key = input()   #암호화 키 입력
lenkey = len(key)   #암호화 키 길이
count = 0   #암호화 키 인덱스

for i in str:
    if i == ' ':    #공백일 경우, 공백 출력
        print(' ', end='')
        count = count_reset(count, lenkey)
    else:   #암호문 출력
        print(cipher(i,key[count]), end='')
        count = count_reset(count, lenkey)