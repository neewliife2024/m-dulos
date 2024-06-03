import math
num = int(input('Digite um número: '))
raiz =  math.sqrt(num)
###print('A raiz de {}, é igual há {}'.format(num, math.ceil(raiz))) #arredondando para cima
print('A raiz de {}, é igual há {}'.format(num, math.floor(raiz))) 

