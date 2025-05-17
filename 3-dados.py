import sqlite3
#1-Conectando no BD
conexao= sqlite3.connect('titulo.db')
cursor= conexao.cursor()

#2- Inserindo dados
cursor.execute(
    """
INSERT INTO filmes(nome, ano,nota)
VALUES ('Sonic',2020,8)
INSERT INTO filmes(nome, ano,nota)
VALUES ('Toy Story',1995,9)
INSERT INTO filmes(nome, ano,nota)
VALUES ('Toy Story 3',2010,9)
   """
)

conexao.commit()
conexao.close()
print("Dados inseridos na tabela")