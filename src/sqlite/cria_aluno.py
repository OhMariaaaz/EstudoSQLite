import os
import schooldb
os.system('clear')

print('Lets register a student')
name = input('What is the name of the student? ')
room = int(input('Where is this students study room? '))

result = schooldb.cria_aluno(name, room)
print(result)
