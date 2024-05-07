import FreeSimpleGUI as sg
from zip_extractor import extract_archive
# Text is a type (starts with a capital letter
# Text("Select destination folder") in an instance of Text
sg.theme("DarkPurple4")
label1 = sg.Text("Select Archive")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="file")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

output_label = sg.Text(key="output", text_color="red", font=('Helvetica', 20))

extract_button = sg.Button("Extract")

window = sg.Window("Archive Extractor",
                   layout=[[label1], [input1, choose_button1],
                           [[label2], [input2, choose_button2]],
                           [extract_button, output_label]])
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(event, values)
    file = values["file"]
    folder = values["folder"]
    print(file)
    print(folder)
    extract_archive(file, folder)
    window["output"].update(value="Process completed successfully!")

window.close()