salário = float(input('Qual o seu salário? R$'))
novo = salário + (salário * 15 / 100)
print('O seu salário de R${:.2f}, com aumento de 15%, agora vale R${:.2f}.'.format(salário, novo))