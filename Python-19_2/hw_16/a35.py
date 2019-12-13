a = input()
code = input()
word = ""
num = 0
number = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
long = len(code)
for i in a:
    if i == " ":
     word+=i
    else:
      if ord(i)-ord(code[num])<=0:
          word += number.get(26+(ord(i)-ord(code[num])))
      else:
          word += number.get(ord(i)-ord(code[num]))
    num+=1
    if num == long:
        num = 0
print(word)