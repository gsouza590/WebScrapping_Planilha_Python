import xlwings as xw

def escrever_planilha(procedimento_nome, procedimento_numero_dois, procedimento_numero_um, documento_nome, documento_numero_um, documento_numero_dois, contra_prova_numero_um, contra_prova_numero_dois, substancia_nome):
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
    ws.range((last_row + 1, 2)).value = procedimento_nome
    ws.range((last_row + 1, 3)).value = procedimento_numero_dois
    ws.range((last_row + 1, 4)).value = procedimento_numero_um
    ws.range((last_row + 1, 5)).value = documento_nome
    ws.range((last_row + 1, 6)).value = documento_numero_um
    ws.range((last_row + 1, 7)).value = documento_numero_dois
    ws.range((last_row + 1, 8)).value = contra_prova_numero_um
    ws.range((last_row + 1, 9)).value = contra_prova_numero_dois
    ws.range((last_row + 1, 12)).value = substancia_nome

    wb.save()

    # Fechar o arquivo Excel
    wb.close()