print("*******************************")
print("........ Encription ...........")
print("-------------------------------")
print("")

Massage = input("Enter Massage :")
#msg="keshan"   //for testing
print("")

counter=0
Encription_Massage=""

for letter in Massage:
    #print(letter)   // for testing
    if (counter==0):
        Encription_Massage=Encription_Massage+letter
        counter=1
    else:
        ascii_code = ord(letter)+counter
        counter=counter+1
        Encription_Massage=Encription_Massage+(chr(ascii_code))

print(f"Encription_Massage : {Encription_Massage}")
print("")
print("*******************************")
