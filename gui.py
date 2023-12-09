
import PySimpleGUI as sg

morse_map = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ", "F": "..-. ",
    "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ",
    "S": "... ", "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
    "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ", "0": "----- "
}

def text_to_morse(userinput):
    morse_code = ''.join(morse_map.get(i.upper(), '') for i in userinput)
    return morse_code

def morse_to_text(userinput):
    userinput = userinput.split("  ")
    decode = ''.join(
        [next(key for key, value in morse_map.items() if value == i) for i in userinput]
    )
    return decode

layout = [
    [sg.Text("Morse Code Translator", font=("Helvetica", 16))],
    [sg.Text("Enter Text or Morse Code: "), sg.InputText(key="user_input")],
    [sg.Button("Translate"), sg.Button("Exit")],
    [sg.Text(size=(40, 1), key="output")]
]

window = sg.Window("Morse Code Translator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Translate":
        user_input = values["user_input"]
        if user_input and user_input[0].upper() in morse_map:
            translated_text = text_to_morse(user_input)
        else:
            translated_text = morse_to_text(user_input)
        window["output"].update(translated_text)

window.close()
