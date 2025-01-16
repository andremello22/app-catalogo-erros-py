from datetime import datetime
from tkinter import messagebox
from dataclasses import dataclass
from clientes import clientes  # Importar a lista de clientes

@dataclass
class ClienteService:
    def __init__(self, clientes=[]):
        self.data_referencia = datetime(2025, 1, 15, 10, 0, 0)
        self.data_formatada = self.data_referencia.strftime('%d/%m/%Y %H:%M:%S')
        self.clientes = clientes
        self.geraTxt()

    def geraTxt(self):
        try:
            with open('Data.txt', 'w') as data:
                data.write(f'{self.data_formatada}\n')
                for cliente in self.clientes:
                    data.write(f"Dias para visita: {cliente['dias_para_visita']}\n")
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao gerar arquivo: {e}')

    def verificaData(self):
        try:
            with open('Data.txt', 'r') as data:
                data_str = data.read().strip()
                data_dia_referencia = datetime.strptime(data_str.split('\n')[0], "%d/%m/%Y %H:%M:%S")
                data_atual = datetime.now()
                diferenca_dias = (data_atual - data_dia_referencia).days
                clientes_atualizados = []
                for cliente in self.clientes:
                    dias_para_visita = cliente['dias_para_visita'] - diferenca_dias
                    cliente_atualizado = {
                        'nome': cliente['nome'],
                        'codigo': cliente['codigo'],
                        'dias_para_visita': dias_para_visita
                    }
                    clientes_atualizados.append(cliente_atualizado)
                    if dias_para_visita <= 0:
                        messagebox.showinfo('Aviso', f'Cliente {cliente["nome"]} venceu a visita em {abs(dias_para_visita)} dias.')
                        self.data_referencia = datetime.now()
                        self.geraTxt()
                return clientes_atualizados
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao verificar data: {e}')
            return []
        finally:
            return clientes_atualizados

