from src.bronze.bronze import BronzeProcess
from src.silver.silver import SilverProcess
from src.gold.gold import GoldProcess

bronze = BronzeProcess(57, 2025)
silver = SilverProcess()
gold = GoldProcess()

bronze.process()
silver.process()
gold.process(silver.arquivo_analise_tratado())