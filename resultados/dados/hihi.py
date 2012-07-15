f = open('resultados[13-07-2012][13-07-2012].csv', 'r')
ff = open('resultados[13-07-2012][13-07-2012]f.csv', 'w')

lines = f.readlines()
f.close()
i = 0
for line in lines:
    line = line[:-1]
    dados = line.split(',')
    dadosf = [str(i)]
    i += 1
    dadosf.extend(dados[:2])
    dadosf.extend(['%s' % str(s) for s in dados[2:]])
    ff.write(','.join(dadosf)+'\n')
ff.close()
