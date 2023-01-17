from random import randint
from time import sleep
computador = randint (0, 5) #faz o computador pensar!
print('-=-' * 20)
print('vou pensar em um numero de 0 a 5, tente advinhar...')
print('-=-' * 20)
jogador = int(input('em que numero pensei?'))# o jogador tenta advinhar!
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('parabéns, você ganhou!')
else:
    print('você perdeu, eu pensei no numero {} e não no numero {}'.format(computador, jogador))
    