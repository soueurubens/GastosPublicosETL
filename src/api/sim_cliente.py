import requests

class SimCliente:
    def __init__(self, codigo_municipio, ano_atuacao):
        self.__url_base = 'https://api-dados-abertos.tce.ce.gov.br/sim'
        self.__codigo_municipio = int(codigo_municipio)
        self.__ano_atuacao = ano_atuacao
    def pega_dados_acesso(self):
        url_dados_municipos = self.__url_base+f'/municipios?codigo_municipio=0{self.__codigo_municipio}'
        response = requests.get(url_dados_municipos)
        response.raise_for_status()
        return response.json()

    def pega_orgaos(self):
        url_dados_orgaos = self.__url_base+f'/orgaos?codigo_municipio=0{self.__codigo_municipio}&exercicio_orcamento={self.__ano_atuacao}00'
        response = requests.get(url_dados_orgaos)
        response.raise_for_status()
        return response.json()

    def pega_orcamento_despesas(self):
        url_dados_despesas = self.__url_base+f'/orcamento_despesa?codigo_municipio=0{self.__codigo_municipio}&exercicio_orcamento={self.__ano_atuacao}00'
        response = requests.get(url_dados_despesas)
        response.raise_for_status()
        return response.json()
    
