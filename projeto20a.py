print('-=' * 20)
print('analisador de triangulos!')
print('-=' * 20)
r1 = float(input('Digite o primeiro seguimento:'))
r2 = float(input('Digite o segundo seguimento:'))
r3 = float(input('Digite o terceiro seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima PODEM FORMAR um triangulo')
else:
    print('Os seguimentos a cima NÃO PODEM FORMAR um triangulo')