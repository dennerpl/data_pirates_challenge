from bs4 import BeautifulSoup
from unidecode import unidecode
import requests
import pandas as pd
from constants import states,data_frame_format


def scrapper(response, uf):
    next_key = 'Localidade'
    site = BeautifulSoup(response.content, 'html.parser')

    tabelas = site.select('table.tmptabela')

    if len(tabelas) > 1:
        infos = tabelas[1].select('table.tmptabela tr td')
    else:
        infos = site.select('table.tmptabela tr td')

    for info in infos:
        data_frame_format[next_key].append(unidecode(info.text))
        if next_key == 'Localidade':
            data_frame_format['UF'].append(uf)
            next_key = 'CEP'
        elif next_key == 'CEP':
            next_key = 'Situacao'
        elif next_key == 'Situacao':
            next_key = 'Tipo'
        elif next_key == 'Tipo':
            next_key = 'Localidade'
    return 'scrapper executado com sucesso'

def post_request(uf, pagini, pagfim):
    try:
        response = requests.post('https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm', data={'UF': uf, 'qtdrow': 50, 'pagini': pagini, 'pagfim': pagfim})
    except:
        print('Parâmetros da requisição incorretos ou endpoint indisponível')
    return response

def next_page_check(response):
    site = BeautifulSoup(response.content, 'html.parser')
    return site.find('a', href="javascript:document.Proxima.submit('Proxima')")


for state in states:
    print(f'Fazendo a raspagem de CEP do estado {state}')
    first_item = 1
    last_item = 50
    request_result = post_request(state, first_item, last_item)
    while next_page_check(request_result):
        scrapper(request_result, state)
        first_item = first_item + 50
        last_item = last_item + 50
        request_result = post_request(state, first_item, last_item)
    if next_page_check(request_result) is None:
        scrapper(request_result, state)


data = pd.DataFrame(data_frame_format)

print(data)
print('Raspagem de dados finalizada com sucesso')

data.to_json('cep_list.json', orient='index')

print('O arquivo cep_list.json foi escrito ou sobrescrito na pasta raiz do projeto')

