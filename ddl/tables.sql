# Cria uma tabela
CREATE TABLE trabalhadores(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    salario REAL NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE departamentos(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
);

# Renomeia uma tabela
RENAME TABLE trabalhadores TO funcionarios

# Altera a estrutura da tabela
ALTER TABLE funcionarios ADD COLUMN carga_horaria INT;
ALTER TABLE funcionarios DROP COLUMN carga_horaria;
ALTER TABLE funcionarios MODIFY COLUMN carga_horaria TIME;
ALTER TABLE funcionarios ALTER COLUMN salario SET DEFAULT 0.0;
ALTER TABLE funcionarios ALTER COLUMN salario DROP DEFAULT;
ALTER TABLE funcionarios MODIFY COLUMN carga_horaria NULL;
ALTER TABLE funcionarios MODIFY COLUMN carga_horaria NOT NULL;
ALTER TABLE funcionarios ADD PRIRMARY KEY (nome);
ALTER TABLE funcionarios ADD CONSTRAINT fk_depto
    FOREIGN KEY (departamento_id) REFERENCES departementos(id);
ALTER TABLE funcionarios ADD CONSTRAINT email_unico UNIQUE (email)
ALTER TABLE funcionarios ADD COLUMN carga_horaria INT

# Apaga os dados da tabela


# Apaga a tabela do db