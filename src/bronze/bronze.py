import json
from pathlib import Path
from src.api.sim_cliente import SimCliente

class BronzeProcess:
    def __init__(self, codigo, ano_atuacao):
        self._sim_cliente = SimCliente(codigo, ano_atuacao)

    def process(self):
        dados_acesso = self._sim_cliente.pega_dados_acesso()
        orcamentos_despesas = self._sim_cliente.pega_orcamento_despesas()
        orgaos = self._sim_cliente.pega_orgaos()

        self.salva_dados('dados_acesso', dados_acesso)
        self.salva_dados('orcamento_despesas', orcamentos_despesas)
        self.salva_dados('orgaos',orgaos)
        

    def salva_dados(self, nome_pasta, dados):
        folder_path = Path(f'data/bronze/{nome_pasta}')
        file_path = folder_path / f'{nome_pasta}.json'
        folder_path.mkdir(exist_ok=True, parents=True)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)

