velocidade = float(input('qual é a velocidade atual do carro:'))
if velocidade > 80:
    print('MULTADO, você excedeu o limite permitido que é de 80 Km/h')
    multa = (velocidade-80) * 7
    print('você deve pagar uma multa no valor de R${:.2f}'.format(multa))
print('tenha um bom dia, DIRIJA COM SEGURANÇA...')