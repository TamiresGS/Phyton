print('Desafio30')
print('')
import random
print('Agora vamos sortear a ordem das apresentações')
a1=input('Digite o nome do aluno:')
a2=input('Digite o nome do outro aluno:')
a3=input('Digite o nome do outro aluno:')
a4=input('Digite o nome do último aluno:')
alunos=[a1,a2,a3,a4]
ordem=random.sample(alunos,4)
print('A ordem das apresentações é essa:,{}.'.format(ordem))

random.shuffle(alunos)
print('A ordem das apresentações:')
print(alunos)
