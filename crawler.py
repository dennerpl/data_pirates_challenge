from bs4 import BeautifulSoup
import requests
import pandas as pd

states = [
   'SP',
   'MG' 
]

result = {
    'UF': [],
    'Localidade': [],
    'CEP': [],
    'Situacao': [],
    'Tipo': []
}


def scrapper(response, uf):
    next_key = 'Localidade'
    site = BeautifulSoup(response.content, 'html.parser')

    tabelas = site.select('table.tmptabela')

    if len(tabelas) > 1:
        infos = tabelas[1].select('table.tmptabela tr td')
    else:
        infos = site.select('table.tmptabela tr td')

    for info in infos:
        result[next_key].append(info.text)
        if next_key == 'Localidade':
            result['UF'].append(uf)
            next_key = 'CEP'
        elif next_key == 'CEP':
            next_key = 'Situacao'
        elif next_key == 'Situacao':
            next_key = 'Tipo'
        elif next_key == 'Tipo':
            next_key = 'Localidade'

def post_request(uf, pagini, pagfim):
    try:
        response = requests.post('https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm', data={'UF': 'SP', 'qtdrow': 50, 'pagini': pagini, 'pagfim': pagfim})
    except:
        print('Parâmetros da requisição incorretos')
    return response

for state in states:
    request_result = post_request(state, 1, 50)
    scrapper(request_result, state)

data = pd.DataFrame(result)

print(data)

