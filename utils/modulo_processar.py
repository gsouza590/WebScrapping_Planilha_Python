def processar_dados(procedimento, documento, contraProva, substancia):
    import re

    # Regex
    NomeRegex = r'\w+'
    NumRegexComPonto = r'\d+\.\d+'
    NumRegexComBarra = r'\d+/\d+'

    # Pegar os exatos dados
    procedimentoNome = re.search(NomeRegex, procedimento[1]).group() if re.search(NomeRegex, procedimento[1]) else ''
    procedimentoNumero = re.search(NumRegexComPonto, procedimento[1]).group().split('.') if re.search(NumRegexComPonto, procedimento[1]) else ''
    procedimentoNumeroUm = procedimentoNumero[0] if procedimentoNumero else ''
    procedimentoNumeroDois = procedimentoNumero[1] if len(procedimentoNumero) > 1 else ''
    documentoNome = re.search(NomeRegex, documento[1]).group() if re.search(NomeRegex,documento[1]) else ''
    documentoNumero = re.search(NumRegexComBarra, documento[1]).group().split('/') if re.search(NumRegexComBarra,documento[1]) else ''
    documentoNumeroUm = documentoNumero[0] if documentoNumero else ''
    documentoNumeroDois = documentoNumero[1] if len(documentoNumero) > 1 else ''
    if len(contraProva) >= 3:
        contraProvaReNumero = re.search(NumRegexComBarra, contraProva[2]).group().split('/') if re.search(
            NumRegexComBarra, contraProva[2]) else ''
        contraProvaReNumeroUm = contraProvaReNumero[0] if contraProvaReNumero else ''
        contraProvaReNumeroDois = contraProvaReNumero[1] if len(contraProvaReNumero) > 1 else ''
    else:
        contraProvaReNumeroUm = ''
        contraProvaReNumeroDois=''
    substanciaNome = re.search(NomeRegex, substancia[1]).group() if re.search(NomeRegex, substancia[1]) else ''

    return (procedimentoNome, procedimentoNumeroDois, procedimentoNumeroUm, documentoNome, documentoNumeroUm, documentoNumeroDois, contraProvaReNumeroUm, contraProvaReNumeroDois, substanciaNome)
