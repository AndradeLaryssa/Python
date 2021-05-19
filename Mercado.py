clientes = 0
quantidades = []
homens = []
mulheres = 0
produto_final = []

while(True):
  codigo = input('Digite aqui o código do cliente: ')
  nome = input('Digite aqui o nome do cliente: ')
  sexo = input('Digite aqui o sexo do cliente[M/F]: ')
  clientes += 1
  if sexo in 'Ff':
    mulheres += 1
  else:
    homens.append(nome)
  while(True):
    produtos = []
    valor = float(input('Digite aqui o valor do produto: '))
    quantidade = int(input('Digite aqui a quantidade do produto: '))
    quantidades.append(quantidade)
    produto = valor * quantidade
    if sexo in 'Mm':
      produtos.append(produto)
    continuar = input('Deseja adicionar mais produtos?[S/N] ')
    if continuar in 'Nn':
      produto_final.append(sum(produtos))
      produtos.clear()
      break
  cont = input('Deseja adicionar outro cliente?[S/N] ')
  if cont in 'Nn':
        break


print(f'A quantidade de produtos vendidos no dia foi de {sum(quantidades)}')
print(f'A média da quantidade de produtos em cada compra foi de {sum(quantidades)/len(quantidades)}')

menor = min(produto_final)
auxiliar = produto_final.index(menor)
homem = homens[auxiliar]
print(f'O homem com o menor valor de compra foi {homem}')

print(f'O percentual de mulheres que fez compras no dia foi de {(mulheres/clientes)*100}%')
