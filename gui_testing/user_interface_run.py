
import PySimpleGUI as sg
from tkinter import filedialog
import webbrowser



# Static Variables
WINDOW_TITLE = ''
INTRODUCTORY_MESSAGE = '''This app is used to select either a CSV or XLS/XLSX file and send the input to a Zebra label printer.'''
HELP_MESSAGE = '''This application accepts any .xlsx / .xls or .csv file and sends each
record as a separate label to your Zebra label printer.

Files must contain either a Container ID or Sample ID (barcode) field as the first field.  
It will then print out values from the next seven (7) fields.  The app will ignore any additional
fields; you should rearrange them as desired.

Sometimes the Zebra printer Internet Protocol (IP) addresses or port numbers are misconfigured.
Please contact IS in order to determine the correct IP address and update the 'Zebra Settings.txt' file accordingly.  
Be sure to provide a friendly name as well...

'''


PRINTERS = {
    'Friendlyname 1':'11.2.3.4.5',
    'Friendlyname 2':'11.2.2.333.4'
}

# Dynamic Variables
filename = None


#   Window settings
sg.change_look_and_feel('DarkBlue1')    # Add a touch of color


# All the stuff inside your window.

layout = [
            [sg.Text(INTRODUCTORY_MESSAGE)],
            [sg.Button('Select File...'),sg.Text('               '*80,key='_INPUT_')],
            [sg.Text('Optional: enter custom text for all labels:'), sg.InputText()],
            [sg.Checkbox('no'), sg.Combo(list(PRINTERS.keys()),default_value='Friendlyname 1')],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Special...'), sg.Button('Help'), sg.Button('Open Site')]
            ]


# Create the Window
window = sg.Window(WINDOW_TITLE, layout)

def process_file(file):
    with open(file) as f:
        file_string = f.read()
        sg.popup(file_string)

def call_site(website):
    print('opening...')
    webbrowser.open(website)



# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break

    elif event in ('Help'):
        sg.popup(HELP_MESSAGE)

    elif event in ('Ok') and (filename == None or not filename.endswith('.csv')):

        if filename == None:
            filename = '.nonexistent'

        sg.popup('The file you selected is a %s file.\nPlease select a csv file.\n\nReport any bugs to Jonathan Rice.' % filename.split('.')[1])


    elif event in ('Ok'):

        process_file(filename)

        if values[1]:
            sg.popup('howdy pardner.',title='You checked the box.',background_color='blue',custom_text='hello there')
            print('the box was checked.  Long live the box.')
        print(PRINTERS[values[2]])
        break

    elif event in ('Select File...'):
        filename = filedialog.askopenfilename()
        print(filename.split('/')[-1])

        window['_INPUT_'].update(filename)
    elif event in ('Special...'):
        sg.popup('You discovered a special button!\n\nGood for you.')
    elif event in ('Open Site'):
        call_site('http://www.google.com')
    else:
        print(window.read())

window.close()