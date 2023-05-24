import os
import PySimpleGUI as sg
import xlwings as xw
from bs4 import BeautifulSoup
import sys
from xlwings.constants import BordersIndex
import configparser
import warnings
import requests
import urllib3


def adicionar_valor_lacre(session, last_row):
    while True:
        layout = [
            [sg.Text("Digite a URL do material para adicionar o valor do Lacpire e pressione"),
             sg.Input(key='url_lacre')],
            [sg.Button('Confirmar')]
        ]
        window = sg.Window('Extrator de Dados Planilha ContraProvas', layout)
        event, values = window.read()
        window.close()

        if event == sg.WINDOW_CLOSED:
            sys.exit()

        wb = xw.Book('Contraprova-Controle.xlsm')
        ws = wb.sheets['Contraprova']
        try:
            url2 = values['url_lacre']
            response = session.get(url2, verify=False).content
            soup = BeautifulSoup(response, 'html.parser')
            lacre = soup.find('span', {'class': 'rotulo'}, text='Lacre:')
            lacre = lacre.find_all_next(string=True) if lacre is not None else ''
            lacre = lacre[2] if lacre else ''
            ws.range((last_row + 1, 10)).value = lacre
            wb.save()
            break
        except Exception:
            sg.popup_error(f"Erro ao extrair dados: Página Invalida")
            continue
