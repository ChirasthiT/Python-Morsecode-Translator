#Programmed by Chirasthi Thennakoon
import PySimpleGUI as sg

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
    decode = ""
    for i in userinput:
        decode += morse_map.get(i)
    return decode
        
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
                
    return decode

layout = [
    [sg.Text("Morse Code Translator", font=("Helvetica", 16), background_color="Black")],
    [sg.Text("Please enter morse code with spaces", font=("Helvetica", 12), background_color="Black")],
    [sg.Text("Enter Text or Morse Code: ", background_color="Black", font=("Helvatica", 13)), sg.InputText(key="user_input", size=(15, 5))],
    [sg.Button("Run", size=(7, 2)), sg.Button("clear", button_color="Green", size=(7, 2)) ,sg.Exit(button_color="Red" , size=(7, 2))],
    [sg.Text(size=(25, 5), key="output", background_color="Black", font=("Helvetica", 25))]
]

window = sg.Window("Morse Code Translator by Chirasthi Thennakoon", layout, background_color="Black")

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    elif event == "clear":
        window["user_input"].update("")
    
    elif event == "Run":
        userinput = values["user_input"]
        if userinput[0].upper() in morse_map:
            userinput = userinput.upper()
            out = text_to_morse(userinput)
        else:
            out = morse_to_text(userinput)
        window["output"].update(out)
           
window.close()    


