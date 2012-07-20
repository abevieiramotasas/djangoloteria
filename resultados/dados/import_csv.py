
from resultados.models import Resultado

import csv
import os
import datetime

def importar():
    FILE_DIR = os.path.dirname(__file__)
    RESULTADOS_PATH = os.path.join(FILE_DIR, 'resultados[19-07-2012][19-07-2012]f.csv')
    datareader = csv.reader(open(RESULTADOS_PATH), delimiter=',')

    for row in datareader:
        id = row[0]
        data = row[1]
        turno = row[2]
        resultado = row[3:]
        r = Resultado()
        data = data.split('/')
        r.data = datetime.date(int(data[2]), int(data[1]), int(data[0]))
        r.turno = turno
        r.premio_1 = resultado[0]
        r.premio_2 = resultado[1]
        r.premio_3 = resultado[2]
        r.premio_4 = resultado[3]
        r.premio_5 = resultado[4]
        r.premio_6 = resultado[5]
        r.premio_7 = resultado[6]
        r.premio_8 = resultado[7]
        r.premio_9 = resultado[8]
        r.premio_10 = resultado[9]
        r.save()
