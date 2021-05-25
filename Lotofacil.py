import random

tupla = (15,16,17,18)
tupla2 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
numeros = []

dezenas = int(input('Digite a quantidade de dezenas que deseja marcar na primeira aposta[15 a 18 números]: '))

while dezenas not in tupla:
    print('Por favor, digite um número dentro do intervalo[15 a 18 números]!')
    dezenas = int(input('Digite a quantidade de dezenas que deseja marcar na primeira aposta[15 a 18 números]: '))

for i in range(dezenas):
    numero = int(input(f'Digite o {i+1}º número [1 a 25, sem repetição]: '))

    while numero not in tupla2:
        print('Por favor, digite um número dentro do intervalo[1 a 25]!')
        numero = int(input(f'Digite o {i+1}º número [1 a 25]: '))
    while numero in numeros:
        print('Você já escolheu esse número, por favor digite outro!')
        numero = int(input(f'Digite o {i+1}º número [1 a 25]: '))

    numeros.append(numero)


surpresinha1 = random.sample(range(1,25),18)
surpresinha2 = random.sample(range(1,25),18)
resultado = random.sample(range(1,25),15)

print(f'Sua aposta: {sorted(numeros)}')
print(f'Surpresinha 1: {sorted(surpresinha1)}')
print(f'Surpresinha 2: {sorted(surpresinha2)}')
print(f'Resultado: {sorted(resultado)}')
