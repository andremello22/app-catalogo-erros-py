import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('bd_catalogo.sqlite')
cursor = conn.cursor()

# Criar a tabela (se ainda não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS catalogo_de_erros (
    id INTEGER PRIMARY KEY,
    modelo TEXT,
    defeito TEXT,
    cod TEXT,
    descricao TEXT
)
''')

# Dicionário com os dados
dicionario = {
    1: {
        'modelo': 't4500',
        'defeito': 'puxando várias folhas pela bandeja mu',
        'cod': '*',
        'descricao': 'feito instalação de pad na bandeja mu'
    },
    2: {
        'modelo': 'if1643',
        'defeito': 'senha de admin perdida',
        'cod': 'sem senha',
        'descricao': 'feito reset geral no equipamento.\npara entrar no menu.\nselecione: copier/function/reset/all'
    },
    3: {
        'modelo': 'mfc8912dw',
        'defeito': 'atolamento de papel fantasma.',
        'cod': '*',
        'descricao': 'O defeito encontrava-se no cabo flat que conecta a placa principal à placa de alta tensão'
    },
    4: {
        'modelo': 'l14150',
        'defeito': 'atolamento de papel e movimentos irregulares do carro de impressão',
        'cod': '*',
        'descricao': 'feito a troca do cabo flat que conecta a placa principal a cabeça de impressão'
    },
    5: {
        'modelo': 'EPSON',
        'defeito': 'IMPRESSÕES ARRASTANDO',
        'cod': '-',
        'descricao': 'LIMPEZA NO DISCO ENCODER E FITA ENCODER'
    },
    7: {
        'modelo': 'todos os modelos',
        'defeito': 'o antivírus bit defender estava bloqueando a comunicação.',
        'cod': 'comunicação de rede',
        'descricao': 'criar regra no firewall do bit defender para ip do equipamento\n'
    }
}

# Inserir os dados do dicionário na tabela
for key, value in dicionario.items():
    cursor.execute('''
    INSERT INTO catalogo_de_erros (id, modelo, defeito, codigo, descricao)
    VALUES (?, ?, ?, ?, ?)
    ''', (key, value['modelo'], value['defeito'], value['cod'], value['descricao']))

# Salvar (commit) as mudanças
conn.commit()

# Fechar a conexão
conn.close()