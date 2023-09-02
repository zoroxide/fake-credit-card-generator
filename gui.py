import PySimpleGUI as sg
import api
# Add a touch of color
sg.theme('DarkAmber')  

# All the stuff inside your window.
layout = [  [sg.Text('Welcome to fake-credit-card-generator', size=(40,2))],
            [sg.Text(key='id')],
            [sg.Text(key='type')],
            [sg.Text(key='number')],
            [sg.Text(key='expire')],
            [sg.Text(key='cvv')],
            [sg.Button('Generate'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('fake-credit-card-generator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == sg.WIN_CLOSED or event == 'Generate':
        window['id'].update("ID:" +api.id)
        window['type'].update("Card type:" +api.cardtype)
        window['number'].update("Card number:" +api.cardnumber)
        window['expire'].update("Expire date:" +api.expire)
        window['cvv'].update("CVV:" +api.cvv)

window.close()

