#nome da cidade, número de carros, motocicletas, acidentes de transito em 2018
acidentes = []
acidentes_2000 = []
acidentes_1000 = []
cidades = []
carros = []
motocicletas = []
while(True):
  cidade = input('Digite aqui o nome da cidade: ')
  cidades.append(cidade)
  carro = int(input('Digite aqui o número de carros de passeios da cidade: '))
  carros.append(carro)
  motocicleta = int(input('Digite aqui o número de motocicletas da cidade: '))
  motocicletas.append(motocicleta)
  acidente = int(input('Digite aqui o número de acidentes de trânsito em 2018: '))
  acidentes.append(acidente)
  if carro >= 2000:
    acidentes_2000.append(acidente)
  if motocicleta >= 1000:
    acidentes_1000.append(acidente)
  continuar = input('Deseja adicionar outra cidade?[S/N] ' )
  if continuar in 'Nn':
    break

#maior e menor índice de acidentes e a cidade que pertence
lista_ordenada = sorted(acidentes)
contador = 1
for chave, valor in enumerate(lista_ordenada):
    print(f'A cidade {cidades[chave]} ficou no {contador}º lugar na lista de maior índice de acidentes')
    contador += 1

#media de carros nas cidades
media_carros = sum(carros)/len(cidades)
print(f'A média de carros nas cidades foi de {media_carros}')

#media de motocicletas nas cidades
media_motos = sum(motocicletas)/len(cidades)
print(f'A média de motocicletas nas cidades foi de {media_motos}')

#media de acidentes em cidades nas cidades com mais de 2000 carros
print(f'A média de acidentes nas cidades com mais de 2000 carros foi de {sum(acidentes_2000)/len(acidentes_2000)}')

#media de acidentes em cidades nas cidades com mais de 1000 motos
print(f'A média de acidentes nas cidades com mais de 1000 motos foi de {sum(acidentes_1000)/len(acidentes_1000)}')
