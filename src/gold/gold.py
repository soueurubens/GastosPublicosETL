from pathlib import Path

class GoldProcess:
    def __init__(self):
        self.folder_path = Path(r'data\gold')

    def process(self, dados):
        file_path = self.folder_path / 'tabela_para_analise.csv'
        dados.to_csv(file_path, index=False)
        