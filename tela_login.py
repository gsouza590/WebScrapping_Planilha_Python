import sys
import warnings

import PySimpleGUI as sg
import requests
import urllib3


def fazer_login():
    while True:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        layout = [
            [sg.Text("Usuário"), sg.Input(key='-USERNAME-')],
            [sg.Text("Senha "), sg.Input(key='-PASSWORD-', password_char='*')],
            [sg.Button('Login'), sg.Button('', image_filename='assets/engrenagem.png', image_size=(24, 24), border_width=0, key='botao',
                       pad=((400, 0), (10, 0)))],
          
        ]

        window = sg.Window('Extrator de Dados Planilha ContraProvas', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()
                sys.exit()

            user = values['-USERNAME-']
            password = values['-PASSWORD-']

            login_data = {
                'usuario': user,
                'senha': password
            }

            # Faça login e salve a sessão
            session = requests.Session()
            sessionResponse = session.post('https://www.ditec.pf.gov.br/sistemas/criminalistica/', data=login_data,
                                           verify=False)

            if 'ou senha incorreta' in sessionResponse.text:
                sg.popup("Usuário e/ou Senha incorretos")

            else:
                window.close()
                return session

        window.close()

