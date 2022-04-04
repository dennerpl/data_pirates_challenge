# Data pirates challenge
O desafio consiste em fazer a raspagem de dados no site dos correios, afim de encontrar a faixa de CEP utilizadas nas cidades de cada estado.

# Tecnologias Utilizadas:
- Python 3

## Dependências
**BeautifulSoup:**
- Biblioteca utilizada para interpretar o html retornado na requisição e buscar as tags necessárias dentro do mesmo.

**unidecode:**
- Utilizado para padronizar os nomes das cidades, removendo acentos e caracteres especiais.

**requests:**
- Utilizado para fazer as requisições no site dos correios.

**requests:**
- Utilizado para fazer as requisições no site dos correios.

**pandas:**
- Utilizado para agrupar os dados em colunas, gerar os ids e gerar o arquivo json.

**pytest:**
- Utilizado para criar e executar os testes unitários.

# Primeiros passos:
Criar um ambiente virtual:
```
python -m venv venv
```
ou
```
py -m venv venv
```

Para ativar o ambiente virtual é necessario executar o arquivo activate.bat ou Activate.ps1, varia conforme o sistema operacional que você utilizar:
```
.\venv\Scripts\activate.bat
```
ou
```
.\venv\Scripts\Activate.ps1
```
Instalar as dependencias do projeto:
```
pip install -r requirements.txt
```

## Utilização

Para utilizar o projeto basta executar o arquivo crawler e aguardar até que o processo seja finalizado:
```
.\crawler.py
```

## Resultados

Um arquivo chamado cep_list.json será gerado e podera ser vista uma previa da base de dados gerada no console

## Testes

Para ativar os testes unitarios:
```
pytest
```
Obs: demora para chegar os resultados dos testes mas eles chegam
