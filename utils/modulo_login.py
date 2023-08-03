import PySimpleGUI as sg
import sys
import configparser
import warnings
import requests
import urllib3

image_path = 'utils/engrenagem.png'

def fazer_login():
    while True:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        layout = [
            [sg.Text("Usuário"), sg.Input(key='-USERNAME-')],
            [sg.Text("Senha "), sg.Input(key='-PASSWORD-', password_char='*')],
            [sg.Button('Login'),
             sg.Button('Caminho...', key='botao',
                       pad=((400, 0), (10, 0)))],

        ]

        window = sg.Window('Extrator de Dados Planilha ContraProvas', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()
                sys.exit()

            if event == 'botao':
                configura_caminho()

            if event == 'Login':

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


def configura_caminho():
    config = configparser.ConfigParser()

    layout = [
        [sg.Text('Selecione o caminho da planilha:')],
        [sg.Input(key='arquivo'), sg.FileBrowse()],
        [sg.Button('OK')]
    ]

    window = sg.Window('Selecionar Arquivo', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
            break

        if event == 'OK':
            config['Config'] = {
                'caminho': values['arquivo']}
            with open('config.ini', 'w') as config_file:
                config.write(config_file)
            sg.popup(f'Caminho salvo com sucesso')
            window.close()

    window.close()
