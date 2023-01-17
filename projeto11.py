largura=float(input('digite uma largura!'))
altura=float(input('digite uma altura!'))
área= largura * altura
print('você tem uma dimensão de {} x {} e {} m²'.format(largura, altura, área))
tinta= área / 2
print('pra pintar essa parede você vai precisar de {} litros de tinta'.format(tinta))