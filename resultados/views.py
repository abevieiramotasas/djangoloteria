import csv
from django.http import HttpResponse
import os

THIS_PATH = os.path.dirname(__file__)
RESULTADOS_PATH = os.path.join(THIS_PATH, 'dados', 'resultados.csv')

def importcsv(request):
    datareader = csv.reader(open(RESULTADOS_PATH), delimiter=',')
    response = ''
    for row in datareader:
        response += str(row)
    return HttpResponse(response)
    
