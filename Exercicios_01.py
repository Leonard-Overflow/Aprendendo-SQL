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

# INSERT
# 4. Insira 3 alunos na tabela alunos usando três chamadas separadas de cursor.execute().
# 5. Insira 3 alunos anterior usando executemany() com uma lista de tuplas.
# 6. Insira 5 funcionários na tabela funcionarios de departamentos diferentes (ex: TI,
# RH, Financeiro) usando executemany().
# 7. Insira 4 produtos na tabela produtos, sendo que dois deles devem ter disponivel = 0.

#cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", ('Felipe',17, 9.5))
# cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", ('Maria Fernanda',16, 7.5))
# cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", ('Vitor Hugo',17, 5.0))

# alunos = [('Pedro', 18, 7.0), ('Bianca', 17, '9.0'), ('Rafaela', 17, 8.0)]
#
# cursor.executemany('''
#     INSERT INTO alunos (nome, idade, nota)
#     VALUES (?, ?, ?)
# ''', alunos)

# funcionarios = [('Anderson', 'TI', 2700.00, 1, 'andy@email.com'),
#                 ('Gustavo', 'Financeiro', 3000.00, 1, 'gustavo@email.com'),
#                 ('Rodrigo', 'Administrativo', 4500.00, 0, 'rodrigo@email.com'),
#                 ('Fernanda', 'Administrativo', 4500.00, 1, 'fer@email.com'),
#                 ('Flavia', 'Financeiro', 3000.00, 1, 'flavia@email.com')]
#
# cursor.executemany('''
#     INSERT INTO funcionarios (nome, departamento, salario, ativo, email)
#     VALUES (?, ?, ?, ?, ?)
# ''', funcionarios)

# produtos = [('Celuar', 2100.00, 35, 1),
#             ('Notebook', 3200.00, 0, 0),
#             ('Capinha', 60.00, 0, 0),
#             ('Fone', 120.00, 15, 1)]
#
# cursor.executemany('''
#     INSERT INTO produtos (nome, preco, estoque, disponivel)
#     VALUES (?, ?, ?, ?)
# ''',  produtos)



conn.commit()
conn.close()