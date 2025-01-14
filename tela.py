from dataclasses import dataclass
from tkinter import Label, ttk, Tk
import tkinter as tk
from banco_de_dados import *

@dataclass
class Tela:
    largura: int = 595
    altura: int = 700

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Tela de cadastro')

        # Estilo para os botões
      
        
        # Definir o caminho absoluto para o ícone .ico
        #caminho_icone = 'c:/Users/supor/Documents/App-relatorio/logo-suporte.ico'
        #self.janela.iconbitmap(caminho_icone)
        
        self.centralizar_janela(self.largura, self.altura)
        self.janela.resizable(False, False)
        
        self.lb_titulo = Label(
            self.janela,
            text=" Tela de catálogo de erros",
            font=("Arial", "20", "bold"),
            fg="black",
        )
        self.lb_titulo.grid(row=0, column=0, columnspan=3, pady="10", sticky="nsew")
        
        self.lb_tabela_de_erros = Label(
            self.janela,
            text="Tabela de erros",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_tabela_de_erros.grid(row=2, column=0, columnspan=3, pady="40", sticky="nsew")

        self.frame_treeview = ttk.Frame(self.janela)
        self.frame_treeview.grid(row=3, column=0, columnspan=3, pady=20, padx=10, sticky='nsew')
        self.scrollbar = ttk.Scrollbar(self.frame_treeview, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')
        self.tree = ttk.Treeview(self.frame_treeview, columns=('id', 'modelo', 'defeito', 'descricao', 'codigo'), show='headings', yscrollcommand=self.scrollbar.set)
        self.tree.column('id', minwidth=0, width=50)
        self.tree.column('modelo', minwidth=0, width=100)
        self.tree.column('defeito', minwidth=0, width=100)
        self.tree.column('descricao', minwidth=0, width=200)
        self.tree.column('codigo', minwidth=0, width=100)
        self.tree.heading('id', text='ID')
        self.tree.heading('modelo', text='Modelo')
        self.tree.heading('defeito', text='Defeito')
        self.tree.heading('descricao', text='Descrição')
        self.tree.heading('codigo', text='Código')
        self.tree.pack(fill='both', expand=True)
        self.scrollbar.config(command=self.tree.yview)

        self.lb_modelo = Label(
            self.janela,
            text="Modelo",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_modelo.grid(row=4, column=0, pady="10", sticky="nsew")
        self.campoModelo = ttk.Entry(self.janela, font=("Arial", "10"), width=20)
        self.campoModelo.grid(row=4, column=1, pady="10", sticky="nsew")

        self.lb_defeito = Label(
            self.janela,
            text="Defeito",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_defeito.grid(row=5, column=0, pady="10", sticky="nsew")
        self.campoDefeito = ttk.Entry(self.janela, font=("Arial", "10"), width=20)
        self.campoDefeito.grid(row=5, column=1, pady="10", sticky="nsew")

        self.lb_descricao = Label(
            self.janela,
            text="Descrição",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_descricao.grid(row=6, column=0, pady="10", sticky="nsew")
        self.campoDescricao = ttk.Entry(self.janela, font=("Arial", "10"), width=20)
        self.campoDescricao.grid(row=6, column=1, pady="10", sticky="nsew")

        self.lb_codigo = Label(
            self.janela,
            text="Código",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_codigo.grid(row=7, column=0, pady="10", sticky="nsew")
        self.campoCodigo = ttk.Entry(self.janela, font=("Arial", "10"), width=20)
        self.campoCodigo.grid(row=7, column=1, pady="10", sticky="nsew")

        self.bt_cadastrar = tk.Button(
            self.janela,
            text="Cadastrar",
            width=20,
            fg='white',
            bg='green'
            
         
           
        )
        self.bt_cadastrar.grid(row=8, column=0,  )

        self.btn_alterar = tk.Button(
            self.janela,
            text="Alterar",
            width=20,
            fg='white',
            bg='blue'
          
            
        )
        self.btn_alterar.grid(row=8, column=1,  padx="20")

        self.btn_excluir = tk.Button(
            self.janela,
            text="Excluir",
            width=20,
            fg='white',
            bg='red'
           
          
            
        )
        self.btn_excluir.grid(row=8, column=2,  padx="20")



        self.janela.mainloop()

    def centralizar_janela(self, largura, altura):
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()
        x = int((screen_width / 2) - (largura / 2))
        y = int((screen_height / 2) - (altura / 2))
        self.janela.geometry(f'{largura}x{altura}+{x}+{y}')

    def inserir(self):
        try:
           bd = BancoDeDados()
           bd.inserir_erros(self.campoModelo.get(), self.campoDefeito.get(), self.campoDescricao.get(), self.campoCodigo.get())
        except Exception as e:
            print(f'Erro ao inserir: {e}')

    
    def alterar(self):
        try:
            print("ola")
        except Exception as e:
            print(f'Erro ao alterar: {e}')

    def excluir(self):
        try:
            print("ola")
        except Exception as e:
            print(f'Erro ao excluir: {e}')

    def carregar_dados_tabela(self):
        try:
            bd = BancoDeDados()
        except Exception as e:
            print(f'Erro ao carregar dados na tabela: {e}')
        
        