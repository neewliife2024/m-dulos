## km hm dam m dm cm mm
medida =  float(input('Uma distância em metros: '))
cm = medida * 100
mm =  medida * 1000 
dm = medida  * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A media de {}m corresponde a {}cm e {}mm. \nJá o km equivale há {}'.format(medida, cm, mm, km))
