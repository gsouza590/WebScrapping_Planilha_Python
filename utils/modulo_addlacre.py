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

config = configparser.ConfigParser()
config.read('config.ini')
caminho = config.get('Config', 'caminho')
wb = xw.Book(caminho)
ws = wb.sheets['Contraprova']

def adicionar_valor_lacre(session, last_row, url2):
    while True:
        try:
            response = session.get(url2, verify=False).content
            soup = BeautifulSoup(response, 'html.parser')
            lacre = soup.find('span', {'class': 'rotulo'}, text='Lacre:')
            lacre = lacre.find_all_next(string=True) if lacre is not None else ''
            lacre = lacre[2] if lacre else ''
            ws.range((last_row + 1, 10)).value = lacre
            wb.save()
            break
        except Exception:
            sg.popup_error(f"Erro ao extrair dados: Página Inválida")
            break
