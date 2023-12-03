#Programmed by Chirasthi Thennakoon

morse_map = {
    "A":". -  ",
    "B":"- . . .  ",
    "C":"- . - .  ",
    "D":"- . .  ",
    "E":".  ",
    "F":". . - .  ",
    "G":"- - .  ",
    "H":". . . .  ",
    "I":". .  ",
    "J":". - - -  ",
    "K":"- . -  ",
    "L":". - . .  ",
    "M":"- -  ",
    "N":"- .  ",
    "O":"- - -  ",
    "P":". - - .  ",
    "Q":"- - . -  ",
    "R":". - .  ",
    "S":". . .  ",
    "T":"-  ",
    "U":". . -  ",
    "V":". . . -  ",
    "W":". - -  ",
    "X":"- . . -  ",
    "Y":"- . - -  ",
    "Z":"- - . .  ",
    "1":". - - - -  ",
    "2":". . - - -  ",
    "3":". . . - -  ",
    "4":". . . . -  ",
    "5":". . . . .  ",
    "6":"- . . . .  ",
    "7":"- - . . .  ",
    "8":"- - - . .  ",
    "9":"- - - - .  ",
    "0":"- - - - -  "
}

def text_to_morse(userinput):
    for i in userinput:
        print(morse_map.get(i), end="")
        
def morse_to_text(userinput:str):
    userinput = userinput.split("  ")
    morse_list = []
    decode = ""
    
    for i in userinput:
        i += "  "
        morse_list.append(i)

    for i in morse_list:
        for key, value in morse_map.items():
            if i == value:
                decode += key
                
    print(decode)
        
print("""
      111        111   1111111   1111111   111111   1111111      1111111  1111111  1111111   1111111
      1111      1111   11   11   11   11   11       11           11       11   11  11    11  11 
      11 11    11 11   11   11   11 11       1111   1111         11       11   11  11     1  1111
      11  11  11  11   11   11   11   11       11   11           11       11   11  11    11  11
      11    11    11   1111111   11    11  111111   1111111      1111111  1111111  1111111   1111111
      """)

print("To exit press ctrl+c \n")
        
while True:
    try:
        userinput = input("Enter the text : ")
        if userinput[0].upper() in morse_map:
            userinput = userinput.upper()
            text_to_morse(userinput)
            print("\n")
        else:
            morse_to_text(userinput)
            print("\n")

    except KeyboardInterrupt:
        quit("Thank you for using mrse-cde-Trnsltr!")














