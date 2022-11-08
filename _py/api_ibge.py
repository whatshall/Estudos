import requests
Url = 'https://servicodados.ibge.gov.br/api/docs/agregados?versao=3#api-bq'
Data = requests.get(Url).json()
print(Data)