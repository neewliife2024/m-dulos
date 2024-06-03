real =  float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.25
print('Possuindo R${}, você pode comprar até ${:.2f} USD '.format(real, dolar))
