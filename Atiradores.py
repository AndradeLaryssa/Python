atiradores = []
nomes = []
distancias = []
sexos = []
acertou_M = []
distancias_F = []

# quantidade de participantes, nome, sexo, distância
quantidade = int(input('Digite aqui a quantidade de participantes: '))

while quantidade > 0:
    nome = input('Digite aqui o nome do policial: ')
    nomes.append(nome)
    sexo = input('Digite aqui o sexo do policial[M/F]: ')
    sexos.append(sexo)
    distancia = float(input('Digite aqui a distância(em centímetros) em relação ao alvo: '))
    distancias.append(distancia)
    if distancia < 1:
        atiradores.append(distancia)
    if sexo in 'Ff':
        distancias_F.append(distancia)
    if sexo in 'Mm':
        if distancia == 0:
            acertou_M.append(distancia)

    quantidade -= 1

# melhor atirador/pior atirador
melhor = min(distancias)
auxiliar_1 = distancias.index(melhor)
policial_1 = nomes[auxiliar_1]
sexo_1 = sexos[auxiliar_1]

pior = max(distancias)
auxiliar_2 = distancias.index(pior)
policial_2 = nomes[auxiliar_2]
sexo_2 = sexos[auxiliar_2]



print(f'O percentual de policiais que alcançaram o título de atiradores de elite foi de {(len(atiradores) / len(nomes))*100 :.2f}%')
print(f'O melhor atirador foi {policial_1}, do sexo {sexo_1}, com a distância de {melhor} em relação ao alvo')
print(f'O pior atirador foi {policial_2}, do sexo {sexo_2}, com a distância de {pior} em relação ao alvo')
print(f'A quantidade de homens que acertou o alvo foi de {len(acertou_M)}')
if len(distancias_F) != 0:
  print(f'A média da distância ao alvo obtida pelas atiradoras foi de {sum(distancias_F)/len(distancias_F)}')
