import random

estudantes = []
dados = []
primeiro_ano = 0

contador = 0
while contador < 12:
    nome = input(f'Digite o nome do {contador+1}º estudante: ')
    dados.append(nome)
    idade = int(input(f'Digite a idade do {contador+1}º estudante: '))
    dados.append(idade)
    ano = int(input('Digite o ano que o mesmo está cursando [1 a 3]: '))
    if ano == 1:
        primeiro_ano += 1
    dados.append(ano)
    estudantes.append(dados[:])
    dados.clear()
    contador += 1

random.shuffle(estudantes)


print(f'Equipe A: Nome:{estudantes[0][0]}, Idade: {estudantes[0][1]}, Ano:{estudantes[0][2]}'
      f'\nNome:{estudantes[1][0]}, Idade: {estudantes[1][1]}, Ano:{estudantes[1][2]}'
      f'\nNome:{estudantes[2][0]}, Idade: {estudantes[2][1]}, Ano:{estudantes[2][2]}')
mediaA = (estudantes[0][1] + estudantes[1][1] + estudantes[2][1])/3
print(f'Média de idade entre os estudantes da Equipe A: {mediaA :.2f}')
terceiroA = 0
if estudantes[0][2] == 3:
    terceiroA += 1
if estudantes[1][2] == 3:
    terceiroA += 1
if estudantes[2][2] == 3:
    terceiroA += 1
print(f'Quantidade de estudantes do 3º ano na Equipe A: {terceiroA}')

print(f'Equipe B: Nome:{estudantes[3][0]}, Idade: {estudantes[3][1]}, Ano:{estudantes[3][2]}'
      f'\nNome:{estudantes[4][0]}, Idade: {estudantes[4][1]}, Ano:{estudantes[4][2]}'
      f'\nNome:{estudantes[5][0]}, Idade: {estudantes[5][1]}, Ano:{estudantes[5][2]}')
mediaB = (estudantes[3][1] + estudantes[4][1] + estudantes[5][1])/3
print(f'Média de idade entre os estudantes da Equipe B: {mediaB :.2f}')
terceiroB = 0
if estudantes[3][2] == 3:
    terceiroB += 1
if estudantes[4][2] == 3:
    terceiroB += 1
if estudantes[5][2] == 3:
    terceiroB += 1
print(f'Quantidade de estudantes do 3º ano na Equipe B: {terceiroB}')

print(f'Equipe C: Nome:{estudantes[6][0]}, Idade: {estudantes[6][1]}, Ano:{estudantes[6][2]}'
      f'\nNome:{estudantes[7][0]}, Idade: {estudantes[7][1]}, Ano:{estudantes[7][2]}'
      f'\nNome:{estudantes[8][0]}, Idade: {estudantes[8][1]}, Ano:{estudantes[8][2]}')
mediaC = (estudantes[6][1] + estudantes[7][1] + estudantes[8][1])/3
print(f'Média de idade entre os estudantes da Equipe C: {mediaC :.2f}')
terceiroC = 0
if estudantes[6][2] == 3:
    terceiroC += 1
if estudantes[7][2] == 3:
    terceiroC += 1
if estudantes[8][2] == 3:
    terceiroC += 1
print(f'Quantidade de estudantes do 3º ano na Equipe C: {terceiroC}')


print(f'Equipe D: Nome:{estudantes[9][0]}, Idade: {estudantes[9][1]}, Ano:{estudantes[9][2]}'
      f'\nNome:{estudantes[10][0]}, Idade: {estudantes[10][1]}, Ano:{estudantes[10][2]}'
      f'\nNome:{estudantes[11][0]}, Idade: {estudantes[11][1]}, Ano:{estudantes[11][2]}')
mediaD = (estudantes[9][1] + estudantes[10][1]+ estudantes[11][1])/3
print(f'Média de idade entre os estudantes da Equipe D: {mediaD :.2f}')
terceiroD = 0
if estudantes[9][2] == 3:
    terceiroD += 1
if estudantes[10][2] == 3:
    terceiroD += 1
if estudantes[11][2] == 3:
    terceiroD += 1
print(f'Quantidade de estudantes do 3º ano na Equipe D: {terceiroD}')

print(f'Percentual de alunos do Primeiro Ano: {(primeiro_ano/12)*100 :.2f}%')
