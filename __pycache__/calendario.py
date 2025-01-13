from datetime import datetime, timedelta
from dataclasses import dataclass

@dataclass
class Calendario:
    data: str
    def __init__(self):
        self.obter_data_atual()

    def obter_data_atual(self):
        self.data = datetime.now()
        self.data = self.data.strftime('%Y-%m-%d %H:%M:%S')
        print(f'Data e hora atual do sistema: {self.data}')

    def calcular_alarme(self):
        data_alarme = self.data + timedelta(days=17)
        data_alarme_formatada = data_alarme.strftime('%Y-%m-%d %H:%M:%S')
        return data_alarme_formatada



