import sqlite3

# Abre o arquivo .sql em modo leitura e aramzena o resultado em "sql"
with open("tables.sql", "r") as f:
    sql = f.read()

# Cria o arqivo se não existir e abre ele
conn = sqlite3.connect("empresa.db")
cursor = conn.cursor()

# Executa o arquivo .sql e fecha a conexão
cursor.execute(sql)
conn.commit()
conn.close()