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

# Selecionando dados
#cursor.execute("SELECT * FROM usuarios WHERE salario = 3000")

# Ler dados específicos
#cursor.execute("SELECT nome, email FROM usuarios")

# Usando AS
#cursor.execute("SELECT * FROM (SELECT COUNT(*) AS total_de_usuarios FROM usuarios) AS total") cria outra tabela temporaria chamada total com uma colunas total de usuarios

# Usando ORDER BY
#cursor.execute("SELECT * FROM usuarios ORDER BY nome ASC") Crescnte. Padrão pode omitir o ASC
#cursor.execute("SELECT * FROM usuarios ORDER BY nome DESC") Decrescente.
#cursor.execute("SELECT nome, localizacao, email FROM usuarios ORDER BY 2") organiza por localizacao
#cursor.execute("SELECT * FROM usuarios ORDER BY  email ASC NULLS LAST/FIRST")

# Limitando resultados

# Usando Subquerries

# Usando UNION
#cursor.execute("SELECT nome FROM clientes UNION SELECT nome FROM fornecedores") remove as  duplicatas
#cursor.execute("SELECT nome FROM clientes UNION ALL SELECT nome FROM fornecedores") matem as  duplicatas

# Window functions

# ATUALIZANDO DADOS(UPDATE)

# Atualizando a estrutura da tabela

# cursor.execute("ALTER TABLE usuarios ADD COLUMN id INTEGER")

# Atualizar um valor único

#cursor.execute("UPDATE usuarios SET idade = 18 WHERE nome = 'Leonardo'")

# Atualizar várias colunas

#cursor.execute("UPDATE usuarios SET idade = 18, localizacao = 'Campinas', salario = 1700.00, status = 1 WHERE nome = 'Pedro'")

# Atualizar com condição

# cursor.execute('''
#     UPDATE usuarios SET salario = CASE
#         WHEN id  IN (1, 2) THEN 4500.00
#         WHEN id  IN (5, 6) THEN 3500.00
#         WHEN status IS null THEN 1
#     END;
# ''')

# Com base no valor atual

#cursor.execute("UPDATE usuarios SET salario = salario * 1.15 WHERE id = 2 or 3")

# Com subquerry

# cursor.execute('''
#     UPDATE usuarios
#     SET salario = (SELECT AVG(salario) FROM usuarios)
#     WHERE nome =  'Thomas Nield'
# ''')

# Lista com vários valores

# cursor.execute('''
#     UPDATE usuarios
#     SET status = 0
#     WHERE nome IN ('Vitor', 'Rafael', 'Julio')
# ''')



# DELETE

# Deletando dados específicos
#cursor.exeute("DELETE FROM usuarios WHERE id = 10")
#cursor.exeute("DELETE FROM usuarios WHERE nome = 'Leonardo'")
#cursor.exeute("DELETE FROM usuarios WHERE email = julio@email.com")

# Limpando tabelas
#cursor.execute("DELETE FROM clientes")
#cursor.execute("TRUNCATE TABLE usuarios")

# Deletando tabelas
#cursor.execute("DROP TABLE usuarios")
#cursor.execute("DROP TABLE IF EXISTES usuarios") Apaga com verificação

# Envia as modificações para o banco
conn.commit()

# Fecha conexão
conn.close()