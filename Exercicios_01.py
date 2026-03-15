import sqlite3

# Exercícios que o Claude gerou pra mim com base no arquivo crud.py(ainda incompleto).

conn = sqlite3.connect('Escola.db')
cursor = conn.cursor()

# Conexão e Criação de Tabelas
# 1. Crie uma conexão com um banco chamado escola.db e crie uma tabela
# alunos com as colunas: id, nome, idade e nota (REAL).
# 2. Crie uma tabela produtos com as colunas: id, nome, preco (REAL),
# estoque (INTEGER) e disponivel (INTEGER para simular boolean).
# 3. Crie uma tabela funcionarios com: id, nome, departamento,
# salario (REAL) e ativo (INTEGER). Em seguida, use ALTER TABLE para
# adicionar a coluna email.

# cursor.execute('''
#     CREATE TABLE alunos(
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         idade INTEGER NOT NULL,
#         nota REAL NOT NULL
#     );
# ''')

# cursor.execute('''
#     CREATE TABLE produtos (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         preco REAL NOT NULL,
#         estoque INTEGER NOT NULL,
#         disponivel INTEGER NOT NULL
#     );
# ''')

# cursor.execute('''
#     CREATE TABLE funcionarios (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         departamento TEXT NOT NULL,
#         salario REAL NOT NULL,
#         ativo INTEGER NOT NULL
#     );
# ''')
#
# cursor.execute('''
#         ALTER TABLE funcionarios ADD COLUMN email TEXT NOT NULL;
# ''')



conn.commit()
conn.close()