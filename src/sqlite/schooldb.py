import sqlite3
import os

os.system('clear')
# Criando conexão com o banco de dados.
# Se o banco de dados não existir, ele cria.
connection = sqlite3.connect("escola.db")
cursor = connection.cursor()

# cursor.execute(
#    "CREATE TABLE Aluno (nomeAluno TEXT, numSalaAluno INTEGER)"
#    )


def cria_aluno(name, room):
    cursor.execute(
        "INSERT into Aluno values (?, ?)", (name, room))
    result = cursor.execute(
                "SELECT nomeAluno, numSalaAluno FROM Aluno"
                ).fetchall()
    connection.commit()
    connection.close()
    return result
