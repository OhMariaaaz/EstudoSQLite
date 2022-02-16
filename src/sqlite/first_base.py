# Estudos de SQLite.
import sqlite3
import os
from contextlib import closing

os.system('clear')
# Criando conexão com o banco de dados.
# Se o banco de dados não existir, ele cria.
with closing(sqlite3.connect("escola.db")) as connection:
    with closing(connection.cursor()) as cursor:

        # Criando tabela e realizando algumas inserções.
        # cursor.execute("CREATE TABLE Aluno (nomeAluno TEXT, numSalaAluno
        # INTEGER)")
        cursor.execute("INSERT into Aluno VALUES ('Roberto', 1)")
        cursor.execute("INSERT into Aluno VALUES ('Alana', 7)")

        # Buscando TODOS os valores da tabela.
        # Fectall() pega todos os valores que resultam do Select.
        result = cursor.execute(
                "SELECT nomeAluno, numSalaAluno FROM Aluno"
                ).fetchall()
        print(result)

        # Inserindo valores na tabela.
        name = 'Alann'
        cursor.execute(
            "INSERT into Aluno (nomeAluno, numSalaAluno) values (?,?)",
            (name, 3)
            ).fetchall()

        # Atualizando valores na tabela.
        correct_name = 'Alan'
        cursor.execute(
            "UPDATE Aluno SET nomeAluno = ? WHERE nomeAluno = ?",
            (correct_name, name))

        # Buscando um valor especifico da tabela.
        result = cursor.execute(
            "SELECT nomeAluno, numSalaAluno FROM Aluno where numSalaAluno = 3"
            ).fetchall()
        print(result)
