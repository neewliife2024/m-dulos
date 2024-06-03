### nome = input('Qual é seu nome? ')
### print('Prazer em te conhecer {}!'.format(nome))
### print('Prazer em te conhecer {:>20}!'.format(nome)) 20 espaços a direita
### print('Prazer tem te conhecer {:^20}!'.format(nome)) 20 espaçoes mas centralizado

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2 # com ponto flutuante
di = n1 // n2 # divisão inteira
e = n1 ** n2 # exponenciação
# \n irá pular a linha

print('A soma é {}, \n o produto é {}, \n e a divisão é {:.2f}'.format(s, m, d), end=' ')
print('A divisãi inteira é {}, \n e a multiplicação é {}'.format(di, e))
 
# print('A soma vale {}'.format(n1+n2)) 




