'''co = float(input('digite o cumprimento do cateto oposto:'))
ca = float(input('digite o cumprimento do cateto adjacente:'))
hi = (co ** 2) + (ca ** 2) ** (1/2)
print('a hipotenusa é {:.2f}'.format (hi))'''
from math import hypot
co=float(input('digite o cateto oposto:'))
ca=float(input('digite o cateto adjacente:'))
hi= hypot (co, ca)
print('a hipotenusa é {:.2f}'.format(hi))