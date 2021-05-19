#numero do carro, nome do piloto, tempo em segundos, número de punições
numeros = []
nomes = []
tempos_competicao = [] 
tempos_provas = []

while(True):
  print('Para encerar a leitura digite um número negativo')
  numero_carro = int(input('Digite aqui o número do carro: '))
  
  if numero_carro < 0:
    break
  else:
    numeros.append(numero_carro)

  nome_piloto = input('Digite aqui o nome do piloto: ')
  nomes.append(nome_piloto)
  tempo_prova = int(input('Digite aqui o tempo em que a prova foi realizada[Em segundos]: '))
  tempos_provas.append(tempo_prova)
  punicoes = int(input('Digite aqui o número de punições recebidas: '))
  
  if punicoes > 0:
    #punição = adiciona 5% no tempo de prova
    tempo_punicoes = tempo_prova + (tempo_prova * punicoes * (5/100))
    tempos_competicao.append(tempo_punicoes)
  else:
    tempos_competicao.append(tempo_prova)

print(f'Quantidade de carros participantes: {len(numeros)}')

#ordenar em ordem crescente 
lista_ordenada = sorted(tempos_competicao)
contador = 1
for chave, valor in enumerate(lista_ordenada):
    print(f'O {contador}ºLUGAR foi do CARRO {numeros[chave]}, do(a) PILOTO {nomes[chave]}, com o TEMPO de {tempos_competicao[chave]}s')
    contador += 1
