obitos = []
positivos = []
cidades = []

while(True):
  print('\nPara interroper a leitura digite o código como -1')
  codigo = int(input('\nDigite o código do estado: '))
  if codigo == -1:
    break
  nome = input('Digite o nome do estado: ')
  cidades.append(nome)
  positivo = int(input('Digite a quantidade de pacientes do estado que testaram positivo: '))
  positivos.append(positivo)
  mortes = int(input('Digite a quantidade de mortos decorrentes do COVID no estado: '))
  obitos.append(mortes)

print(f'A média de obitos nos estados cadastrados foi de {sum(obitos)/len(obitos)}')

maior = max(positivos)
auxiliar = positivos.index(maior)
nomes = cidades[auxiliar]
print(f'O cidade cadastrada com o maior número de óbitos foi {nomes}')

print(f'O percentual de óbitos da primeira cidade cadastrada foi de {(obitos[0]/sum(obitos)*100)}%')

