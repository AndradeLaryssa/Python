quilometros = []
mulheres = []
while True:
    print('\nPara encerrar o programa digite SAIR')
    nome = input('\nDigite o nome do cliente: ')
    if nome == 'Sair' or nome == 'sair' or nome == 'SAIR':
        break
    sexo = input('Digite o sexo do cliente[M/F]: ')
    placa = input('Digite a placa do carro alugado: ')
    km = int(input('Digite a quantidade de quilômetros contratados: '))
    quilometros.append(km)
    dias = int(input('Digite a quantidade de dias contratados: '))
    if sexo in 'Ff' and dias > 7:
        mulheres.append(nome)
    valor = (70 * dias) + (0.10 * km)
    print(f'\nO carro de placa {placa} precisa pagar o valor de {valor} reais')

print(f'A média de quilômetros contratados pelos clientes foi de {sum(quilometros)/len(quilometros)}')
print(f'A(s) cliente(s) do sexo feminino que fechou(ram) aluguel(is) acima de 7 dias foi(ram) {mulheres}')



