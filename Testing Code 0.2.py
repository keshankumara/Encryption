msg="keshan"
a=0
b=[]
for letter in msg:
    print(letter)
    if (a==0):
        ascii_code = ord(letter)
        b.append(ascii_code)
        a=1
    else:
        ascii_code = ord(letter)+a
        a=a+1
        b.append(ascii_code)
print(b)





