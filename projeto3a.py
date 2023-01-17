import math
ângulo=float(input('digite um angulo:'))
seno=math.sin(math.radians(ângulo))
print('o angulo {} tem o seno de {:.2f}'.format(ângulo, seno))
co=math.cos(math.radians(ângulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(ângulo, co))
tan=math.tan(math.radians(ângulo))
print('o ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tan))