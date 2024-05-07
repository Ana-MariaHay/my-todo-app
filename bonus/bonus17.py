# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg
from converters14 import convert

# Text is a type (starts with a capital letter
# Text("Select destination folder") in an instance of Text

sg.theme("DarkPurple4")

label1 = sg.Text("Enter feet  :")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

output_label = sg.Text("", key="output", text_color="red", font=('Helvetica', 10))

window = sg.Window("Convertor",
                   layout=[[label1], [input1],
                           [[label2], [input2,]],
                           [convert_button, exit_button, output_label]])
while True:
    try:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        print(event, values)
        feet = float(values["feet"])
        inches = float(values["inches"])
        meters = convert(feet, inches)
        window["output"].update(value=f"Meters: {meters}")
    except (ValueError, SyntaxError):
        sg.popup("Enter numbers in the input boxes", font=("Helvetica", 10))

window.close()