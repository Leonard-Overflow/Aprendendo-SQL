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

cursor.execute('''DELETE FROM cliente WHERE id = 2''')

cursor.execute("""SELECT * FROM cliente""")
print(cursor.fetchall())

conexao.commit()
conexao.close()