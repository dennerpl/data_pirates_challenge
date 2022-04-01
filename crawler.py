from bs4 import BeautifulSoup
import requests
import pandas as pd

result = {
    'UF': ["SP", "MG"],
    'Localidade': ["São Paulo", "Belo Horizonte"],
    'CEP': [33221564, 21465878],
    'Situacao': ['teste', 'teste'],
    'Faixa': ['faixa1', 'faixa2']
}

next_key = 'Localidade'

response = requests.post('https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm', data={'UF': 'SP', 'qtdrow': 50, 'pagini': 51, 'pagfim': 100})

site = BeautifulSoup(response.content, 'html.parser')

tabelas = site.select('table.tmptabela')

infos = site.select('table.tmptabela tr td')

uf = site.find_all('td', width=10)

for info in infos:
    result[next_key].append(info.text)
    if next_key == 'Localidade':
        result['UF'].append('SP')
        next_key = 'CEP'
    elif next_key == 'CEP':
        next_key = 'Situacao'
    elif next_key == 'Situacao':
        next_key = 'Faixa'
    elif next_key == 'Faixa':
        next_key = 'Localidade'

data = pd.DataFrame(result)

print(data)

