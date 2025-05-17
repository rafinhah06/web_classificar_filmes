import sqlite3

#1- Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#2- Atualizando dados
id = 1
cursor.execute(
    """
UPDATE filmes SET nome = ?
WHERE id = ?
    """,
    ('O Senhor dos Anéis', id)
)
conexao.commit()
print("Dados atualizados")