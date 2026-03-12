import sqlite3

# Conexão com banco
conn = sqlite3.connect('Basico.db') # Conecta com o arquivo do banco
cursor = conn.cursor() # O cursor é o responsavel por executar os scripts SQL
# conn = sqlite3.connect(':memory:') Cria um banco temporario na RAM e apaga quando o programa for fechado

# Criação de tabela
# cursor.execute("""
#      CREATE TABLE usuarios(
#          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#          nome TEXT NOT NULL,
#          email TEXT NOT NULL
#      );
#      """);

# Tipos de dados
# INTEGER
# REAL(Deicmais)
# TEXT
# BLOB(Arquivos brutos que não são texto Ex: .jpg)
# NULL Valor vazio

# Modificando a tabela
# cursor.execute("ALTER TABLE usuarios ADD COLUMN id INTEGER")



# CRIANDO DADOS(CREATE)

# Inserindo valores
#cursor.execute("INSERT INTO usuarios ('nome', 'email') VALUES ('Pedro', 'pedro@email.com')")

# Inserir vários elementos
# dados = [
#     ('Julio', 'julio@email.com'),
#     ('Vitor', 'vitor@email.com'),
#     ('Thomas Nield', 'ThomasNield@email.com')
# ]
#
# cursor.executemany("INSERT INTO usuarios ('nome', 'email') VALUES (?, ?)", dados)



# LENDO(READ)

# Ler toda a tabela
# dados = cursor.execute("SELECT * FROM usuarios")
# print(dados.fetchall())

# Ler itens específicos
dados = cursor.execute('SELECT * FROM usuarios WHERE id = 1')
print(dados.fetchall())
dados2 = cursor.execute('SELECT * FROM usuarios WHERE email = "pedro@email.com"')
print(dados2.fetchall())

# Envia os dados para o banco
conn.commit()

# Fecha conexão
conn.close()