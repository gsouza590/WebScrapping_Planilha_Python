import sys

import PySimpleGUI as sg
from bs4 import BeautifulSoup


def extrair_dados(session):
    while True:
        layout = [
            [sg.Text("Digite a URL do Laudo que deseja extrair as informações:"), sg.Input(key='url')],
            [sg.Button('Extrair Dados')]
        ]
        window = sg.Window('Extrator de Dados Planilha ContraProvas', layout)
        event, values = window.read()
        window.close()

        if event == sg.WINDOW_CLOSED:
            sys.exit()

        url = values['url']

        try:
            response = session.get(url, verify=False).content
            soup = BeautifulSoup(response, 'html.parser')

            # Extração dos dados
            procedimento = soup.find('span', {'class': 'rotulo'}, text='Procedimento: ').find_all_next(string=True)
            documento = soup.find('span', {'class': 'rotulo'}, text='Identificação:').find_all_next(string=True)
            contraProva = soup.find('span', {'class': 'rotulo'}, text='Item:').find_all_next(string=True)
            substancia = soup.find('span', {'class': 'rotulo'}, text='Subclasse').find_all_next(string=True)

            return procedimento, documento, contraProva, substancia
        except Exception:
            sg.popup_error(f"Erro ao extrair dados: Página Invalida")
            continue
