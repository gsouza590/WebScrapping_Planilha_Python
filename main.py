import sys

import PySimpleGUI as sg
import time
import os
from add_lacre import adicionar_valor_lacre
from extracao_dados import extrair_dados
from extrair_informacao_dados import *
from tela_login import fazer_login

session = fazer_login()

while True:
    while True:
        if session is not None:
            dados = extrair_dados(session)
            extrair_informacoes_dos_dados(dados)
            dados_extraidos = extrair_informacoes_dos_dados(dados)
            last_row = atualizar_planilha(dados_extraidos)

            layout = [
                [sg.Text("Gostaria de adicionar o valor do Lacre? S/N"), sg.Input(key='resp')],
                [sg.Button('Confirmar')]
            ]
            window = sg.Window('Extrator de Dados Planilha ContraProvas', layout)
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()

            elif values['resp'].upper() != 'S':
                window.close()
                break
            else:
                window.close()
                adicionar_valor_lacre(session, last_row)

                break
        else:
            sys.exit()

    layout = [
        [sg.Text("Deseja realizar nova extração de Laudo?(S/N)"), sg.Input(key='resp2')],
        [sg.Button('Confirmar')]
    ]

    window = sg.Window('Extrator de Dados Planilha ContraProvas', layout)
    event, values = window.read()
    window.close()

    if values['resp2'].upper() != 'S':
        break
    else:
        os.system('cls')

