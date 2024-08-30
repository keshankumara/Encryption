msg="keshan"
a=0
b=""
for letter in msg:
    print(letter)
    if (a==0):
        b=b+letter
        a=1
    else:
        ascii_code = ord(letter)+a
        a=a+1
        b=b+(chr(ascii_code))
print(b)
