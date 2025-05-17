import sqlite3

#1- conectando no bd
conexao =  sqlite3.connect('titulo.db')

#2- criando o cursor
cursor = conexao.cursor()

#3- criando a tabela
cursor.execute(
    """
CREATE TABLE filmes(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
ano INTEGER NOT NULL,
nota REAL NOT NULL
);
    """
)

#4- fecha conexão
conexao.close()
print("Tabela foi criada")