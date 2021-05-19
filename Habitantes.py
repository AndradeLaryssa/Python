nomes = []
salarios = []
sexos = []
idades = []
habitan = []
mulheres = 0

while(True):
    nome = input('Digite o nome do habitante responsável: ')
    nomes.append(nome)
    salario = int(input('Digite o sálario do responsável: '))
    salarios.append(salario)
    sexo = input('Digite o sexo do responsável[M/F]: ')
    sexos.append(sexo)
    if sexo in 'Ff':
        mulheres += 1
    idade = int(input('Digite a idade do reponsável: '))
    idades.append(idade)
    habitantes = int(input('Digite o número de habitantes no lar: '))
    habitan.append(habitantes)
    continuar = input('Deseja adicionar outro responsável[S/N]? ')
    if continuar in 'Nn':
        break

contador = 0
if salarios[contador] > 1500:
    print(f'Nome: {nomes[contador]}'
          f'\nSalário: {salarios[contador]} reais'
          f'\nSexo: {sexos[contador]}'
          f'\nIdade: {idades[contador]} anos'
          f'\nHabitantes no lar: {habitan[contador]}')
    
    contador += 1

print(f'A média de salário nas residências foi de {sum(salarios)/len(salarios)}')
print(f'O percentual de mulheres que são responsáveis pelos seus lares foi de {(mulheres/len(nomes))*100 :.2f}%')

maior = max(salarios)
auxiliar = salarios.index(maior)
responsavel = nomes[auxiliar]
print(f'O(s) responsável(s) {responsavel} obtiveram o maior salário da pesquisa: {maior} reais')

