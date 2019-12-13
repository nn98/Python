sen=input()
secret=input()
lensec=len(secret)
num=0
secsen=''

asc={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

for i in sen:
    if i==' ':
        secsen += i
    else :
        if ord(i)-ord(secret[num]) <= 0:
            secsen += asc.get(26+(ord(i)-ord(secret[num])))
        else :
            secsen += asc.get(ord(i)-ord(secret[num]))
    num += 1
    if num==lensec:
        num=0
print(secsen)