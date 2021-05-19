tupla = (0,1,2,3,4)
votos = []
windows = []
linux = []
mac = []
outro = []
while(True):
    nome = input('Digite seu nome: ')
    print('Qual o melhor Sistema Operacional?'
          '\n1 - Windows'
          '\n2 - Linux'
          '\n3 - Mac'
          '\n4 - Outro')
    print('\nPara interromper a leitura, informe o voto 0')
    voto = int(input('Digite seu voto [0 a 4]: '))
    if voto == 0:
        break
    if voto == 1:
        windows.append(voto)
    if voto == 2:
        linux.append(voto)
    if voto == 3:
        mac.append(voto)
    if voto == 4:
        outro.append(voto)
    elif voto not in tupla:
        print('Digite apenas números dentro do intervalo [0 a 4]')
    else:
        votos.append(voto)

print(f'O total de votos computados foi de {len(votos)}')
print(f'Windows = {len(windows)} votos '
      f'\nLinux = {len(linux)} votos '
      f'\nMac = {len(mac)} votos '
      f'\nOutro = {len(outro)} votos')
print(f'Windows = {len(windows)/len(votos)}% votos '
      f'\nLinux = {len(linux)/len(votos)}% votos '
      f'\nMac = {len(mac)/len(votos)}% votos '
      f'\nOutro = {len(outro)/len(votos)}% votos')

if len(windows) > len(linux) and len(windows) > len(mac) and len(windows) > len(outro):
    print('O sistema mais votado foi o Windows')
if len(linux) > len(windows) and len(linux) > len(mac) and len(linux) > len(outro):
    print('O sistema mais votado foi o Linux')
if len(mac) > len(windows) and len(mac) > len(linux) and len(mac) > len(outro):
    print('O sistema mais votado foi o Mac')
if len(outro) > len(windows) and len(outro) > len(linux) and len(outro) > len(mac):
    print('O sistema mais votado foi Outro')

