# -*- encoding: utf-8 -*-
import urllib2
import re
import datetime
import time
from resultados.models import Resultado


def craw(data_i, data_f=None):
    if data_f is None:
        data_f = data_i
    RESULTADO_RE = re.compile(r'<div class="numeros">[^0-9]*?([0-9]*?)[^0-9]*?</div>')
    DATA_RE = re.compile(r'(\d{1,})')

    URL_BASE = 'http://www.lotece.com.br/v2/?page_id=70&data='

    ONE_DAY = datetime.timedelta(1)

    # gero os date
    data_inicial = datetime.date(*[int(s) for s in DATA_RE.findall(data_i)][::-1])
    data_final = datetime.date(*[int(s) for s in DATA_RE.findall(data_f)][::-1])

    data = data_inicial

    todos_resultados = {}
    # itero nos dias
    while data <= data_final:
        # constroi a url
        data_as_string = data.strftime('%d/%m/%Y')    
        url_completa = URL_BASE+data_as_string
        # baixa a pagina
        pagina = urllib2.urlopen(url_completa).read()
        # captura os resultados
        resultados = RESULTADO_RE.findall(pagina)
        # adiciona aos resultados
        todos_resultados[data] = {}
        # nao teve jogo
        if len(resultados) == 0:
            data += ONE_DAY
            continue
        if len(resultados) == 10: # apenas um horario
            todos_resultados[data][2] = resultados
        else: # dois resultados
            todos_resultados[data][1] = resultados[:10]
            # 10:20 e nao 10: pois a pagina carrega tanto resultados do dia quanto do anterior
            todos_resultados[data][2] = resultados[10:20]
        # incremento o dia
        data += ONE_DAY
    print(str(todos_resultados))
    for data in todos_resultados.keys():
        if 2 in todos_resultados[data]:
            r = Resultado.objects.filter(data=data, turno=2)
            if len(r) is 0:
                r = Resultado()
                r.data = data
                r.turno = 2
                r.premio_1 = todos_resultados[data][2][0]
                r.premio_2 = todos_resultados[data][2][1]
                r.premio_3 = todos_resultados[data][2][2]
                r.premio_4 = todos_resultados[data][2][3]
                r.premio_5 = todos_resultados[data][2][4]
                r.premio_6 = todos_resultados[data][2][5]
                r.premio_7 = todos_resultados[data][2][6]
                r.premio_8 = todos_resultados[data][2][7]
                r.premio_9 = todos_resultados[data][2][8]
                r.premio_10 = todos_resultados[data][2][9]
                r.save()
        if 1 in todos_resultados[data]:
            r = Resultado.objects.filter(data=data, turno=1)
            if not len(r) is 0:
                continue
            r = Resultado()
            r.data = data
            r.turno = 1
            r.premio_1 = todos_resultados[data][1][0]
            r.premio_2 = todos_resultados[data][1][1]
            r.premio_3 = todos_resultados[data][1][2]
            r.premio_4 = todos_resultados[data][1][3]
            r.premio_5 = todos_resultados[data][1][4]
            r.premio_6 = todos_resultados[data][1][5]
            r.premio_7 = todos_resultados[data][1][6]
            r.premio_8 = todos_resultados[data][1][7]
            r.premio_9 = todos_resultados[data][1][8]
            r.premio_10 = todos_resultados[data][1][9]
            r.save()
