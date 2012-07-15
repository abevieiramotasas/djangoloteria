# -*- encoding: utf-8 -*-
import urllib2
import re
import datetime
import time

# verificando o tempo de execucao
time_inicial = time.time()
# verificando o tempo de execucao

RESULTADO_RE = re.compile(r'<div class="numeros">[^0-9]*?([0-9]*?)[^0-9]*?</div>')
DATA_RE = re.compile(r'(\d{2,})')

URL_BASE = 'http://www.lotece.com.br/v2/?page_id=70&data='

DATA_INICIAL = '13/07/2012'
DATA_FINAL = '13/07/2012'

ONE_DAY = datetime.timedelta(1)

# gero os date
data_inicial = datetime.date(*[int(s) for s in DATA_RE.findall(DATA_INICIAL)][::-1])
data_final = datetime.date(*[int(s) for s in DATA_RE.findall(DATA_FINAL)][::-1])

data = data_inicial

todos_resultados = {}
# itero nos dias
while data <= data_final:
    # constroi a url
    data_as_string = data.strftime('%d/%m/%Y')    
    url_completa = URL_BASE+data_as_string
    print(url_completa, time.time() - time_inicial)
    # baixa a pagina
    pagina = urllib2.urlopen(url_completa).read()
    # captura os resultados
    resultados = RESULTADO_RE.findall(pagina)
    # adiciona aos resultados
    todos_resultados[data_as_string] = {}
    # nao teve jogo
    if len(resultados) == 0:
        data += ONE_DAY
        continue
    if len(resultados) == 10: # apenas um horario
        todos_resultados[data_as_string][1] = resultados
    else: # dois resultados
        todos_resultados[data_as_string][1] = resultados[:10]
        # 10:20 e nao 10: pois a pagina carrega tanto resultados do dia quanto do anterior
        todos_resultados[data_as_string][2] = resultados[10:20]
    # incremento o dia
    data += ONE_DAY

f = open('resultados[%s][%s].csv' % (DATA_INICIAL.replace('/','-'), DATA_FINAL.replace('/','-')), 'w')
# gerar um .csv
LINE = '%s,%s,%s\n'
for data in todos_resultados.keys():
    if 1 in todos_resultados[data]:
        resultados = ','.join(todos_resultados[data][1])
        line = LINE % (data, '1', resultados)
        f.write(line)
    if 2 in todos_resultados[data]:
        resultados = ','.join(todos_resultados[data][2])
        line = LINE % (data, '2', resultados)
        f.write(line)
f.close() 
print(time.time() - time_inicial, 'seconds')
# print(todos_resultados[datetime.date.today().strftime('%d/%m/%Y')])
