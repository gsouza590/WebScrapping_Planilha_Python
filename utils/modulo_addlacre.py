import xlwings as xw
from bs4 import BeautifulSoup


def adicionar_lacre(session, wb):
    addLacre = input("Gostaria de adicionar o valor do Lacre? S/N ")

    if addLacre.upper() == 'S':
        url = input("Digite a URL do material para adicionar o valor do Lacre e pressione Enter: ")
        response = session.get(url, verify=False).content
        soup = BeautifulSoup(response, 'html.parser')
        lacre = soup.find('span', {'class': 'rotulo'}, text='Lacre:')
        lacre = lacre.find_all_next(string=True) if lacre is not None else ''
        lacre = lacre[2] if lacre else ''

        ws = wb.sheets['Contraprova']
        last_row = ws.range('A1').current_region.last_cell.row
        ws.range((last_row + 1, 10)).value = lacre
        wb.save()
