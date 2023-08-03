
from utils.modulo_addlacre import *
from utils.modulo_extracao import *
from utils.modulo_login import *

session = fazer_login()

while True:
    layout = [
        [sg.Text("Digite a URL do Laudo:")],
        [sg.Input(key='url')],
        [sg.Text("Digite a URL do material para adicionar o valor do Lacre")],
        [sg.Input(key='url_lacre')],
        [sg.Button('Extrair Dados')]
    ]
    window = sg.Window('Extrator de Dados Planilha ContraProvas', layout)
    event, values = window.read()
    window.close()

    if event == sg.WINDOW_CLOSED:
        sys.exit()

    url = values['url']
    url2 = values['url_lacre']
    if session is not None:
        dados = extrair_dados(session, url)
        dados_extraidos = extrair_informacoes_dos_dados(dados)
        last_row = atualizar_planilha(dados_extraidos)
        adicionar_valor_lacre(session, last_row, url2)
        sg.popup('Extração concluída com sucesso!')
    else:
        sys.exit()
