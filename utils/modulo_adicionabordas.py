import xlwings as xw


def adicionar_bordas(sheet, row):
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

    wb.save()
