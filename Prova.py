tupla = ('A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e')
gabarito = []
gabarito_alunos = []
notas = []
nomes = []
matriculas = []
contador = 0

while contador < 6:
    questoes = input(f'Digite o gabarito da {contador + 1}º questão: ')
    questoes.upper()
    #roda novamente quantas vezes forem necessárias
    while questoes not in tupla:
        print('Sua resposta foi inválida! Digite apenas A,B,C,D ou E')
        questoes = input(f'Digite o gabarito da {contador + 1}º questão: ')
        questoes.upper()

    gabarito.append(questoes)
    contador += 1

alunos = int(input('Qual a quantidade de alunos que realizaram a prova? '))

cont = 0
while cont < alunos:
    matricula = input(f'Digite a matrícula do {cont + 1}º aluno: ')
    matriculas.append(matricula)
    nome = input(f'Digite o nome do {cont + 1}º aluno: ')
    nomes.append(nome)
    for i in range(6):
        respostas = input(f'Digite a resposta da {i + 1}º questão: ')
        respostas.upper()
        # roda novamente quantas vezes forem necessárias
        while respostas not in tupla:
            print('Sua resposta foi inválida! Digite apenas A,B,C,D ou E')
            respostas = input(f'Digite a resposta da {i + 1}º questão: ')
            respostas.upper()

        gabarito_alunos.append(respostas)

    nota = 0
    if gabarito[0] == gabarito_alunos[0]:
        nota += 1.5
    if gabarito[1] == gabarito_alunos[1]:
        nota += 1.5
    if gabarito[2] == gabarito_alunos[2]:
        nota += 1.5
    if gabarito[3] == gabarito_alunos[3]:
        nota += 1.5
    if gabarito[4] == gabarito_alunos[4]:
        nota += 2
    if gabarito[5] == gabarito_alunos[5]:
        nota += 2

    notas.append(nota)

    nota = 0
    cont += 1

print(f'Gabarito da prova: {gabarito}')
for chave, valor in enumerate(notas):
    print('\nRelátorio das Notas:'
        f'\nAluno {nomes[chave]}'
        f'\nMatrícula {matriculas[chave]}'
        f'\nNota: {notas[chave]}')

maior = max(notas)
auxiliar = notas.index(maior)
aluno = nomes[auxiliar]
print(f'O(s) aluno(s) {nomes} obtiveram a maior nota da turma: {maior} pontos')

media = sum(notas)/alunos
print(f'A média das notas da turma foi de {media}')

contad = 0
maiores_notas = 0
if notas[contad] > media:
    maiores_notas += 1
    contad += 1
else:
    contad += 1

print(f'O percentual de alunos que obtiveram nota acima da média foi de {(maiores_notas/alunos)*100 :.2f}%')






