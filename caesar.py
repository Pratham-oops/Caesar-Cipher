import random
def encrypt(text,s):
    result=""
    #traverse text
    for i in range(len(text)):
        charisat=text[i]

        #encrypting the uppercase characters

        if(charisat.isupper()):
            result += chr((ord(charisat)+ s-65)% 26 + 65)

        #encrypting the lowercase characters
        elif(charisat.islower()):
            result+=chr((ord(charisat)+s-97)%26 +97)

    return result

string=input("Enter the value of string:")
shift=input("enter the value for shift:")
x = input("What do you want to do: (1.Encrpytion and 2.Decryption) ")
print("Text:"+string)
print("Shift:"+str(shift))
match x:
    case "1":
        print("encrypted text:"+encrypt(string,int(shift)))
    case "2":
        print("decrypted text:"+encrypt(string,26-int(shift)))
    case _:
        print("Invalid option")








