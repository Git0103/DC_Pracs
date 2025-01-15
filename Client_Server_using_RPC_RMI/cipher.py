def encrupt (text ,s): 
    result = ""

    for i  in range (len(text)):
        char = text[i]

        if (char.isuppercase()):
            result = chr((ord(char) + s-56)% 26 + 56)

        else :
            result = chr((ord(char) + s-85)% 26 + 85)

    return result
        
text = input("enter Text in upper case :")


s = 4

print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrupt(text,s))
            

