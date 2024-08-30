print("*******************************")
print("........ Decription ...........")
print("-------------------------------")
print("")

Encripted_Massage = input("Enter Encripted Massage :")
#Encripted_Massage="kfukes"  // For testing
counter=0
print("")
Decripted_Massage=""

for letter in Encripted_Massage:
    #print(letter)    // For testing
    if (counter==0):
        Decripted_Massage=Decripted_Massage+letter
        counter=1
    else:
        #print(f"Previous ASCII No : {ord(letter)}  Previouse Letter :{letter}")   // For testing
        ascii_code = ord(letter)-counter
        #print(f"ASCII Code :{ascii_code}    Letter :{chr(ascii_code)}   Counter :{counter}")   // For testing
        counter = counter + 1
        Decripted_Massage=Decripted_Massage+(chr(ascii_code))

print(f"Decripted Massage : {Decripted_Massage}")
print("")
print("*******************************")
