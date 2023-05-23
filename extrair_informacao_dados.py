
import re

import xlwings as xw
from xlwings.constants import BordersIndex




def extrair_informacoes_dos_dados(dados):
    procedimento, documento, contraProva, substancia = dados

    # Regex
    NomeRegex = r'\w+'
    NumRegexComPonto = r'\d+\.\d+'
    NumRegexComBarra = r'\d+/\d+'

    # Pegar os exatos dados
    procedimentoNome = re.search(NomeRegex, procedimento[1]).group() if re.search(NomeRegex, procedimento[1]) else ''
    procedimentoNumero = re.search(NumRegexComPonto, procedimento[1]).group().split('.') if re.search(NumRegexComPonto,
                                                                                                      procedimento[
                                                                                                          1]) else ''
    procedimentoNumeroUm = procedimentoNumero[0] if procedimentoNumero else ''
    procedimentoNumeroDois = procedimentoNumero[0]+procedimentoNumero[1] if len(procedimentoNumero) > 1 else ''
    documentoNome = re.search(NomeRegex, documento[1]).group() if re.search(NomeRegex, documento[1]) else ''
    documentoNumero = re.search(NumRegexComBarra, documento[1]).group().split('/') if re.search(NumRegexComBarra,
                                                                                                documento[1]) else ''
    documentoNumeroUm = documentoNumero[0] if documentoNumero else ''
    documentoNumeroDois = documentoNumero[1] if len(documentoNumero) > 1 else ''

    if len(contraProva) >= 3:
        contraProvaReNumero = re.search(NumRegexComBarra, contraProva[2]).group().split('/') if re.search(
            NumRegexComBarra, contraProva[2]) else ''
        contraProvaReNumeroUm = contraProvaReNumero[0] if contraProvaReNumero else ''
        contraProvaReNumeroDois = contraProvaReNumero[1] if len(contraProvaReNumero) > 1 else ''
    else:
        contraProvaReNumeroUm = ''
        contraProvaReNumeroDois = ''

    substanciaNome = re.search(NomeRegex, substancia[1]).group() if re.search(NomeRegex, substancia[1]) else ''

    return procedimentoNome, procedimentoNumeroDois, procedimentoNumeroUm, documentoNome, documentoNumeroUm, documentoNumeroDois, contraProvaReNumeroUm, contraProvaReNumeroDois, substanciaNome


def atualizar_planilha(dados):
    procedimentoNome, procedimentoNumeroDois, procedimentoNumeroUm, documentoNome, documentoNumeroUm, documentoNumeroDois, contraProvaReNumeroUm, contraProvaReNumeroDois, substanciaNome = dados

    wb = xw.Book('Contraprova-Controle.xlsm')
    ws = wb.sheets['Contraprova']

    # Encontra a última linha preenchida
    last_row = ws.range('A1').current_region.last_cell.row
    last_index = ws.range('A1').end('down').row
    nextIndex = ws.range((last_index, 1)).value

    if nextIndex is not None:
        nextIndex += 1
    else:
        nextIndex = 1

    # Escreve as informações nas células correspondentes na próxima linha vazia
    ws.range((last_row + 1, 1)).value = nextIndex
    ws.range((last_row + 1, 2)).value = procedimentoNome
    ws.range((last_row + 1, 3)).value = procedimentoNumeroDois
    ws.range((last_row + 1, 4)).value = procedimentoNumeroUm
    ws.range((last_row + 1, 5)).value = documentoNome
    ws.range((last_row + 1, 6)).value = documentoNumeroUm
    ws.range((last_row + 1, 7)).value = documentoNumeroDois
    ws.range((last_row + 1, 8)).value = contraProvaReNumeroUm
    ws.range((last_row + 1, 9)).value = contraProvaReNumeroDois
    ws.range((last_row + 1, 12)).value = substanciaNome

    # Adicionar as bordas às células de 1 a 13
    sheet = xw.books.active.sheets.active
    row = sheet.range('A1').current_region.last_cell.row
    for i in range(1, 14):
        borders = sheet.cells(row, i).api.Borders(xw.constants.BordersIndex.xlEdgeTop)
        borders.LineStyle = xw.constants.LineStyle.xlContinuous
        borders.ColorIndex = xw.constants.ColorIndex.xlColorIndexAutomatic
        borders = sheet.cells(row, i).api.Borders(xw.constants.BordersIndex.xlEdgeBottom)
        borders.LineStyle = xw.constants.LineStyle.xlContinuous
        borders.ColorIndex = xw.constants.ColorIndex.xlColorIndexAutomatic

        if i in [1, 4, 7, 9, 10, 11, 12, 13]:
            borders = sheet.cells(row, i).api.Borders(xw.constants.BordersIndex.xlEdgeRight)
            borders.LineStyle = xw.constants.LineStyle.xlContinuous
            borders.ColorIndex = xw.constants.ColorIndex.xlColorIndexAutomatic

    # Salva as mudanças no arquivo de Excel
    wb.save()
    return last_row
