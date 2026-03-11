import sqlite3


#conexao = sqlite3.connect(':memory:') Cria um banco temporaria na Ram, quando o programa encerra apaga tudo. Útil pra testes rápidos.

# Conexao abre a porta para o banco de dados
conexao = sqlite3.connect('cliente.db')

# Cursor é quem executa os scripts. Pode executar um script(.execute), retornar todos os resultados(.fetchall) ou 1 resultado(.fetchone)
cursor = conexao.cursor()

# Criação de tabela
# cursor.execute("""
#      CREATE TABLE cliente (
#          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#          nome TEXT NOT NULL,
#          email TEXT NOT NULL,
#          senha TEXT NOT NULL
#      );
#  """)

# varios_inserts = [
#     ('Apolo', 'Apolo@gmail.com', '45685698'),
#     ('Eric', 'Eric@gmail.com', '12345678'),
#     ('Paulo', 'Paulo@gmail.com', '81579723')
# ]

# O executemany executa vários scripts de uma vez
# cursor.executemany("INSERT INTO cliente (nome, email, senha) VALUES (?, ?, ?)", varios_inserts)

# rowid mostra o id da linha, mas eu já havia criado a propriedade id
#cursor.execute("""SELECT rowid, * FROM cliente""")

cursor.execute("""SELECT * FROM cliente WHERE id = "" """)

tabela = cursor.fetchall()

for item in tabela:
     print(item)

#print(cursor.fetchall())

# many para vários
#print(cursor.fetchmany(2))

# one para apenas um a partr de um id. Para pegar uma linha específica é necessário usar WHERE
#print(cursor.fetchone())

# Imprime os itens sparando por linha formatando
# tabela = cursor.fetchall()
#
# for item in tabela:
#     print(item[1] + "\t\t" + item[2])

# Para enviar as mudanças(insert, update, delete, etc) utiliza-se o commit, igual em um código no git hub
conexao.commit()
conexao.close()