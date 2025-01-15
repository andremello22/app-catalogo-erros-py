
import sqlite3 as connect


class BancoDeDados:
    conexao = None
    cursor = None

    def __init__(self):
      self.criarTabeCatalogo()

    def criarTabeCatalogo(self):
        try:
            self.conexao = connect.connect("bd_catalogo.sqlite")
            self.cursor = self.conexao.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS catalogo_de_erros('id' INTEGER PRIMARY KEY, 'modelo' TEXT , 'defeito' TEXT , 'descricao' TEXT, 'codigo' TEXT)''')
            self.conexao.commit()
            print("Tabela criada com sucesso!")
        except connect.Error as e:
            print(f"Erro ao conectar ao banco de dados!\nerro:{e}")
        finally:
            self.cursor.close()
            self.conexao.close()
            print("Banco de dados desconectado com sucesso!!")



 
    def inserirErros(self, modelo, defeito, descricao, codigo):
        try:
            conexao = connect.connect("bd_catalogo.sqlite")
            cursor = conexao.cursor()
            cursor.execute('''INSERT INTO catalogo_de_erros(modelo, defeito, descricao, codigo) VALUES(?, ?, ?,?)''', (modelo, defeito, descricao, codigo))
            conexao.commit()
        
        except connect.Error as e:
            print(f"Erro ao inserir dados!\nErro:{e}")

        finally:
            cursor.close()
            conexao.close()
            print("Banco de dados desconectado com sucesso!!")




  
    def selecionarErros(self):
        try:
            conexao = connect.connect("bd_catalogo.sqlite")
            cursor = conexao.cursor()
            cursor.execute('''SELECT * FROM catalogo_de_erros''')
            conexao.commit()
            lista = cursor.fetchall()
            return lista
        except connect.Error as e:
            print(f"Erro ao ler dados!\nErro:{e}")

        finally:
            cursor.close()
            conexao.close()
            print("Banco de dados desconectado com sucesso!!")
  
  


    def editarErros(self, id, modelo, defeito, descricao, codigo):
        try:
            conexao = connect.connect("bd_catalogo.sqlite")
            cursor = conexao.cursor()
            cursor.execute('''UPDATE catalogo_de_erros SET modelo = ?, defeito = ?, descricao = ?, codigo = ? WHERE id = ?''', (modelo,defeito,descricao,codigo ,id))
            conexao.commit()
        
        except connect.Error as e:
            print(f"Erro ao editar dados!\nErro:{e}")
        
        finally:
            cursor.close()
            conexao.close()
            print("Banco de dados desconectado com sucesso!!")



    def excluirErros(self, id):
        try:
            conexao = connect.connect("bd_catalogo.sqlite")
            cursor = conexao.cursor()
            cursor.execute('''DELETE FROM catalogo_de_erros WHERE id = ?''', (id,))
            conexao.commit()
            
        except connect.Error as e:
            print(f"Erro ao excluir dados!\nErro:{e}")

        finally:
            cursor.close()
            conexao.close()
            print("Banco de dados desconectado com sucesso!!")







  
