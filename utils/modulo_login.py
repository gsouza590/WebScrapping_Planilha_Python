import getpass
import warnings
import requests
import urllib3



def realiza_login():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    while True:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        user = input("Insira o usuario: ")
        password = getpass.getpass(prompt='Digite sua senha: ')

        login_data = {
            'usuario': user,
            'senha': password
        }

        # Faça login e salve a sessão
        session = requests.Session()
        sessionResponse = session.post('https://www.ditec.pf.gov.br/sistemas/criminalistica/', data=login_data,
                                       verify=False)

        if 'ou senha incorreta' in sessionResponse.text:
            print("Usuário e/ou Senha incorretos")
        else:
            break

        return session