from django.core.management import setup_environ
import settings
setup_environ(settings)

from resultados.models import Resultado

import csv

datareader = csv.reader(open('resultados.csv'), delimiter=',')

for row in datareader:
    print(str(row))
