import requests
from bs4 import BeautifulSoup


def extrair_dados(session, url):
    while True:
        while True:
            try:
                # Acesse a página desejada com a sessão autenticada
                url = input("Digite a URL do Laudo que deseja extrair as informações após pressione Enter: ")
                response = session.get(url, verify=False).content
                soup = BeautifulSoup(response, 'html.parser')

                # Extração dos dados
                try:
                    procedimento = soup.find('span', {'class': 'rotulo'}, text='Procedimento: ').find_all_next(
                        string=True)
                except AttributeError:
                    procedimento = ''

                try:
                    documento = soup.find('span', {'class': 'rotulo'}, text='Identificação:').find_all_next(string=True)
                except AttributeError:
                    documento = ''

                try:
                    contraProva = soup.find('span', {'class': 'rotulo'}, text='Item:').find_all_next(string=True)
                except AttributeError:
                    contraProva = ''

                try:
                    substancia = soup.find('span', {'class': 'rotulo'}, text='Subclasse').find_all_next(string=True)
                except AttributeError:
                    substancia = ''

                return procedimento, documento, contraProva, substancia

                break

            except requests.exceptions.RequestException as e:
                print(f"Erro ao acessar página: {e}")
            except ValueError as e:
                print(f"Erro ao processar dados: {e}")

            return None, None, None, None
