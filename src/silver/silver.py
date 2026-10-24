import json
from pathlib import Path
import pandas as pd
from src.api.sim_cliente import SimCliente

class SilverProcess:
    def __init__(self):
        self._save_folder_path = Path('data/silver/dados_processados')

        self._file_dados_acesso = Path('data/bronze/dados_acesso/dados_acesso.json')
        self._file_orcamento_despesas = Path('data/bronze/orcamento_despesas/orcamento_despesas.json')
        self._file_orgaos = Path('data/bronze/orgaos/orgaos.json')

    def process(self):
        self.dados_acesso_tratados(self._file_dados_acesso)
        self.orgaos_tratados(self._file_orgaos)
        self.orcamentos_despesas_tratados(self._file_orcamento_despesas)

    def dados_acesso_tratados(self, arquivo):
        with open(arquivo, 'r', encoding='utf-8') as file:
            data = json.load(file)['elements'][0]
        cod_municipio = data['codigo_municipio']
        nome_municipio = data['nome_municipio']
        dados_tratados = {
            'codigo_municipio': cod_municipio,
            'nome_municipio': nome_municipio
        }


        self.salva_dados(dados_tratados, 'dados_acesso')

    def orgaos_tratados(self, arquivo):
        # Codigo_municipio 
        # codigo_orgao 
        # nome_orgao 
        dados_tratados = []
        with open(arquivo, 'r', encoding='utf-8') as file:
            data = json.load(file)['elements']

        for elemento in data:
            codigo = elemento['codigo_municipio']
            codigo_orgao = elemento['codigo_orgao']
            nome_orgao = elemento['nome_orgao']

            dados = {'codigo_municipio': codigo, 
                     'codigo_orgao':codigo_orgao,
                     'nome_orgao': nome_orgao}
            dados_tratados.append(dados)

        self.salva_dados(dados_tratados, 'orgaos')

    def orcamentos_despesas_tratados(self, arquivo):
        # CODIGO MUNICIPIO 
        # CODIGO ORGAO
        # CODIGO UNIDADE ORCAMENTARIA
        # NOME ELEMENTO DESPESA
        # VALOR_TOTAL_FIXADO
        dados_tratados = []
        with open(arquivo, 'r', encoding='utf-8') as file:
            data = json.load(file)['elements']

        for elemento in data:
            cod_municipio = elemento['codigo_municipio']
            cod_orgao = elemento['codigo_orgao']
            cod_unidade = elemento['codigo_unidade_orcamentaria']
            nome_elemento_despesa = elemento['nome_elemento_despesa']
            valor_total_fixado = elemento['valor_total_fixado']

            dado = {
                'codigo_municipio': cod_municipio,
                'codigo_orgao':cod_orgao,
                'codigo_unidade_orcamentaria':cod_unidade,
                'nome_elemento_despesa': nome_elemento_despesa,
                'valor_total_fixado':valor_total_fixado
            }
            dados_tratados.append(dado)

        self.salva_dados(dados_tratados, 'orcamento_despesas')


    def arquivo_analise_tratado(self):
        dados_acessos = r'data\silver\dados_processados\dados_acesso.json'
        with open(dados_acessos, 'r', encoding='utf-8') as file: 
            data = json.load(file)

        df_dado_acesso = pd.DataFrame([data])

        df_orgaos = pd.read_json(r'data\silver\dados_processados\orgaos.json')
        df_orgaos['codigo_municipio'] = df_orgaos['codigo_municipio'].astype(str)

        df_orcamento_despesas = pd.read_json(r'data\silver\dados_processados\orcamento_despesas.json')
        df_orcamento_despesas = df_orcamento_despesas.astype(str)

        # print("DADOS: \n")
        # print(df_dado_acesso.dtypes)
        # print("ORGAOS: \n")
        # print(df_orgaos.dtypes)
        # print("ORCAMENTO: \n")
        # print(df_orcamento_despesas.dtypes)

        orcamentos_despesas_orgaos = pd.merge(df_orgaos,df_orcamento_despesas, on='codigo_municipio', how='left')
        return orcamentos_despesas_orgaos
        
     
    def salva_dados(self, dados, nome_arquivo):
        folder_path = self._save_folder_path
        folder_path.mkdir(exist_ok=True, parents=True)
        file_path = folder_path / f'{nome_arquivo}.json'
        with open(file_path, 'w', encoding='utf-8') as file: 
            json.dump(dados, file, indent=4, ensure_ascii=False)
        

