print("*******************************")
print("...........Welcome ............")
print("-------------------------------")
print("")

print("If you want to Encript : Enter Number 01")
print("If you want to Decript : Enter Number 02")
selection_number = input("Enter Number :")
print("")

if (int(selection_number)==1):
    print("*******************************")
    print("........ Encription ...........")
    print("-------------------------------")
    print("")

    Massage = input("Enter Massage :")
    # msg="keshan"   //for testing
    print("")

    counter = 0
    Encription_Massage = ""

    for letter in Massage:
        # print(letter)   // for testing
        if (counter == 0):
            Encription_Massage = Encription_Massage + letter
            counter = 1
        else:
            ascii_code = ord(letter) + counter
            counter = counter + 1
            Encription_Massage = Encription_Massage + (chr(ascii_code))

    print(f"Encription_Massage : {Encription_Massage}")
    print("")

elif (int(selection_number)==2):
    print("*******************************")
    print("........ Decription ...........")
    print("-------------------------------")
    print("")

    Encripted_Massage = input("Enter Encripted Massage :")
    # Encripted_Massage="kfukes"  // For testing
    counter = 0
    print("")
    Decripted_Massage = ""

    for letter in Encripted_Massage:
        # print(letter)    // For testing
        if (counter == 0):
            Decripted_Massage = Decripted_Massage + letter
            counter = 1
        else:
            # print(f"Previous ASCII No : {ord(letter)}  Previouse Letter :{letter}")   // For testing
            ascii_code = ord(letter) - counter
            # print(f"ASCII Code :{ascii_code}    Letter :{chr(ascii_code)}   Counter :{counter}")   // For testing
            counter = counter + 1
            Decripted_Massage = Decripted_Massage + (chr(ascii_code))

    print(f"Decripted Massage : {Decripted_Massage}")
    print("")
else:
    print("")
    print("Please Check Your Number again '1/2'")
    print("")
print("*******************************")