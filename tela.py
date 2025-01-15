from banco_de_dados import BancoDeDados
from tkinter import messagebox
from tkinter import ttk, Tk, Label
import tkinter as tk
from dataclasses import dataclass
from calendario import ClienteService
from clientes import clientes

@dataclass
class Tela:
    largura: int = 1400
    altura: int = 700
    dias_para_alerta: int = 0

    def __init__(self):
        self.cliente = clientes
       # print(self.cliente)
        self.janela = Tk()
        self.janela.title('App-catalogo-de-erros')

        # Definir o caminho absoluto para o ícone .ico
        caminho_icone = "D:\\python_poo\\app-catalogo-erros-py-main\\logo-suporte.ico"
        self.janela.iconbitmap(caminho_icone)
        
        self.centralizar_janela(self.largura, self.altura)
        self.janela.resizable(True, True)
        
        self.lb_titulo = Label(
            self.janela,
            text="catálogo de erros",
            font=("Arial", "20", "bold"),
            fg="black",
        )
        self.lb_titulo.grid(row=0, column=0, columnspan=4, pady="10", sticky="nsew")
        
        self.lb_tabela_de_erros = Label(
            self.janela,
            text="Tabela de erros",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_tabela_de_erros.grid(row=1, column=0, columnspan=4, pady="10", sticky="nsew")

        self.frame_treeview = ttk.Frame(self.janela)
        self.frame_treeview.grid(row=2, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')
        self.scrollbar = ttk.Scrollbar(self.frame_treeview, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')
        self.tree = ttk.Treeview(self.frame_treeview, columns=('id', 'modelo', 'defeito', 'descricao', 'codigo'), show='headings', yscrollcommand=self.scrollbar.set)
        self.tree.column('id', minwidth=0, width=50)
        self.tree.column('modelo', minwidth=0, width=200)
        self.tree.column('defeito', minwidth=0, width=200)
        self.tree.column('descricao', minwidth=0, width=300)
        self.tree.column('codigo', minwidth=0, width=150)
        self.tree.heading('id', text='ID')
        self.tree.heading('modelo', text='Modelo')
        self.tree.heading('defeito', text='Defeito')
        self.tree.heading('descricao', text='Descrição')
        self.tree.heading('codigo', text='Código')
        self.tree.pack(fill='both', expand=True)
        self.scrollbar.config(command=self.tree.yview)
        self.carregar_dados_tabela()

        self.frame_form = ttk.Frame(self.janela)
        self.frame_form.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

        self.lb_modelo = Label(
            self.frame_form,
            text="Modelo",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_modelo.grid(row=0, column=0, pady="5", sticky="e")
        self.campoModelo = ttk.Entry(self.frame_form, font=("Arial", "10"), width=20)
        self.campoModelo.grid(row=0, column=1, pady="5", sticky="w")

        self.lb_defeito = Label(
            self.frame_form,
            text="Defeito",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_defeito.grid(row=1, column=0, pady="5", sticky="e")
        self.campoDefeito = ttk.Entry(self.frame_form, font=("Arial", "10"), width=20)
        self.campoDefeito.grid(row=1, column=1, pady="5", sticky="w")

        self.lb_descricao = Label(
            self.frame_form,
            text="Descrição",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_descricao.grid(row=2, column=0, pady="5", sticky="e")
        self.campoDescricao = ttk.Entry(self.frame_form, font=("Arial", "10"), width=20)
        self.campoDescricao.grid(row=2, column=1, pady="5", sticky="w")

        self.lb_codigo = Label(
            self.frame_form,
            text="Código",
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.lb_codigo.grid(row=3, column=0, pady="5", sticky="e")
        self.campoCodigo = ttk.Entry(self.frame_form, font=("Arial", "10"), width=20)
        self.campoCodigo.grid(row=3, column=1, pady="5", sticky="w")
        
        self.bt_cadastrar = tk.Button(
            self.frame_form,
            text="Cadastrar",
            width=20,
            fg='white',
            bg='green',
            command=self.inserir
        )
        self.bt_cadastrar.grid(row=4, column=0, pady="10", sticky="e")

        self.btn_alterar = tk.Button(
            self.frame_form,
            text="Alterar",
            width=20,
            fg='white',
            bg='blue',
            command=self.alterar
        )
        self.btn_alterar.grid(row=4, column=1, pady="10", padx="10", sticky="w")

        self.btn_excluir = tk.Button(
            self.frame_form,
            text="Excluir",
            width=20,
            fg='white',
            bg='red',
            command=self.excluir
        )
        self.btn_excluir.grid(row=4, column=2, pady="10", padx="10", sticky="w")

        self.frame_alerta = ttk.Frame(self.janela)
        self.frame_alerta.grid(row=3, column=2, columnspan=2, pady=10, padx=10, sticky='nsew')

        # Nomes de clientes estáticos e dias para visita
    
        clientes_atualizados = self.alertaParaCliente(self.cliente)
        alertas = "\n".join([f"{cliente['nome']} ({cliente['codigo']}): faltam {cliente['dias_para_visita']} dias para a visita" for cliente in clientes_atualizados])
        self.label_alerta = Label(
            self.frame_alerta,
            text=f'Alerta para visita WF-5710:\n{alertas}',
            font=("Arial", "10", "bold"),
            fg="black",
        )
        self.label_alerta.grid(row=0, column=0, pady="5", sticky="e")

        self.janela.grid_rowconfigure(2, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)

        self.janela.mainloop()

    def centralizar_janela(self, largura, altura):
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()
        x = int((screen_width / 2) - (largura / 2))
        y = int((screen_height / 2) - (altura / 2))
        self.janela.geometry(f'{largura}x{altura}+{x}+{y}')

    def inserir(self):
        try:
            if self.campoModelo.get() == "" or self.campoDefeito.get() == "" or self.campoDescricao.get() == "" or self.campoCodigo.get() == "":
                alerta = messagebox.showinfo(
                    title="Alerta", message="Preencha todos os campos")
            else:
                bd = BancoDeDados()
                bd.inserirErros(self.campoModelo.get(), self.campoDefeito.get(), self.campoDescricao.get(), self.campoCodigo.get())
                alerta = messagebox.showinfo(
                    title="Alerta", message="cadastrado com sucesso")
                

                self.limpar_treeview()
                self.carregar_dados_tabela()
                self.campoDefeito.delete(0, 'end')
                self.campoDescricao.delete(0, 'end')
                self.campoModelo.delete(0, 'end')
                self.campoCodigo.delete(0, 'end')
        except Exception as e:
            print(f'Erro ao inserir: {e}')

    def alterar(self):
        try:
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showinfo(title='Alerta', message='Selecione algum erro para editar!')
                return

            if self.campoModelo.get() == "" or self.campoDefeito.get() == "" or self.campoDescricao.get() == "" or self.campoCodigo.get() == "":
                alerta = messagebox.showinfo(
                    title="Alerta", message="Preencha todos os campos")
            else:
                item = self.tree.item(selected_item[0])
                id = item['values'][0]

                bd = BancoDeDados()
                bd.editarErros(id, self.campoModelo.get(), self.campoDefeito.get(), self.campoDescricao.get(), self.campoCodigo.get())
                alerta = messagebox.showinfo(
                    title="Alerta", message="Erro atualizado com sucesso!!")
                

                self.limpar_treeview()
                self.carregar_dados_tabela()
                self.campoDefeito.delete(0, 'end')
                self.campoDescricao.delete(0, 'end')
                self.campoModelo.delete(0, 'end')
                self.campoCodigo.delete(0, 'end')
        except Exception as e:
            print(f"erro: {e}")
            alerta = messagebox.showerror(
                title="Alerta", message="Erro ao editar erro")

    def excluir(self):
        try:
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showinfo(title='Alerta', message='Selecione algum erro para excluir!')
                return

            mensagem = messagebox.askokcancel(title='Excluir', message='Deseja excluir o erro selecionado?')
            if mensagem:
                item = self.tree.item(selected_item[0])
                id = item['values'][0]
                bd = BancoDeDados()
                bd.excluirErros(id)
                messagebox.showinfo(title="Alerta", message="Excluído com sucesso")
                self.limpar_treeview()
                self.carregar_dados_tabela()
        except Exception as e:
            print(f'Erro ao excluir: {e}')

    def carregar_dados_tabela(self):
        try:
            bd = BancoDeDados()
            lista_erros = bd.selecionarErros()
            for erro in lista_erros:
                self.tree.insert('', 'end', values=erro)
        except Exception as e:
            print(f'Erro ao carregar dados na tabela: {e}')
        
    def limpar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def alertaParaCliente(self, clientes):
        cliente_service = ClienteService(clientes)
        clientes_atualizados = cliente_service.verificaData()
        for cliente in clientes_atualizados:
            print(cliente)
        return clientes_atualizados


   