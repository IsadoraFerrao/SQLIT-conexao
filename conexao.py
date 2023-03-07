import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('DROP TABLE produtos')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (1,"Isadora","França","isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (2,"Maria","Salvador","isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (3,"José","Curitiba","isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (4,"Marcia","São Paulo","isa@gmail.com", 123456)')
#cursor.execute('DELETE FROM usuario where id=1')
dados = cursor.execute('SELECT * FROM usuario')
for usuario in dados:
    print(usuario)
#.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="José"')
conexao.commit()
conexao.close

