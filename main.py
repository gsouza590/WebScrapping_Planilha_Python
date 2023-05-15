import os
import time
from utils.modulo_login import realiza_login
from utils.modulo_extracao import extrair_dados
from utils.modulo_processar import processar_dados
from utils.modulo_gravarplanilha import escrever_planilha
from utils.modulo_adicionabordas import adicionar_bordas
from utils.modulo_addlacre import adicionar_lacre


print("=====================================================")
print("Bem Vindo ao Extrator de Dados Planilha ContraProvas ")
print("=====================================================")
print("\n")

while True:
    realiza_login()

    extrair_dados(session, url)

    processar_dados(procedimento, documento, contraProva, substancia)

    escrever_planilha(procedimento_nome, procedimento_numero_dois, procedimento_numero_um, documento_nome, documento_numero_um, documento_numero_dois, contra_prova_numero_um, contra_prova_numero_dois, substancia_nome)
    adicionar_bordas(sheet, row)

    adicionar_lacre(session, wb)

    resposta = input("Deseja realizar nova extração de Laudo? (S/N)")
    if resposta.upper() != 'S':
        break
    else:
        os.system('cls') or None

print('Obrigado. Volte Sempre!!')
time.sleep(1)
