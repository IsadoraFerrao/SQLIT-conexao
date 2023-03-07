import sqlite3

conexao = sqlite3.connect('banco-relacionamentos')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), endereco VARCHAR(100));')
#cursor.execute('CREATE TABLE notas(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, valor INT, id_aluno INT NOT NULL, FOREIGN KEY (id_aluno) REFERENCES alunos(id));')

cursor.execute('CREATE TABLE if not exists categoria (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100));')
# exemplos: eletrônicos, brinquedos, saúde, esporte
# exemplos de produtos: celular, bicicleta, paracetamol, óculos, notebook
cursor.execute('CREATE TABLE if not exists produtos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100));')

cursor.execute('CREATE TABLE if not exists categoria_produtos(categoria_id INT NOT NULL, produto_id INT NOT NULL, FOREIGN KEY (categoria_id)REFERENCES categoria(id), FOREIGN KEY (produto_id) REFERENCES produtos(id), CONSTRAINT pk_cat_prod PRIMARY KEY(categoria_id,produto_id));')

conexao.commit() #enviar as mudanças
conexao.close