# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg

# Text is a type (starts with a capital letter
# Text("Select destination folder") in an instance of Text
label1 = sg.Text("Enter feet  :")
input1 = sg.Input()

label2 = sg.Text("Enter inches:")
input2 = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[label1], [input1],
                           [[label2], [input2,]],
                           [convert_button]])
window.read()
window.close()