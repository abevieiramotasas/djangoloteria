from resultados.models import Resultado
import time
import random

def grupo(milhar):
    return (((int(milhar)-1)%100)/4)+1
        
def constroi_cache(res):
    grupos_cache = []
    for resultado in res:
        grupos_cache.append([grupo(milhar) for milhar in resultado.resultados()])
    return grupos_cache
        
        
def metodo(TIME_MAX):
    time_inicial = time.time()
    max_errors = 0
    
    total = 0

    # inicio com 40
    resultados = Resultado.objects.order_by('-data')[:70]        
    grupos_cache = constroi_cache(resultados)
    while time.time() - time_inicial < TIME_MAX:
        meus_randons = []
        wrong_random = False
        # enquanto nao ocorre um random errado
        position = 0
        while not wrong_random:
            # verificacao de tempo
            if time.time() - time_inicial >= TIME_MAX:
                break
            # gero random
            random_grupo = random.randint(1,25)           
            # verifico se o grupo randomizado saiu no resultado
            wrong_random = True  
            total += 1
            for premio in grupos_cache[position]:
                # achei uma ocorrencia do random nos premios
                if premio == random_grupo:
                    # passo para o proximo resultado
                    position += 1
                    meus_randons.append(random_grupo)
                    wrong_random = False
                    break            
        # atualizo o numero maximo de erros
        if position > max_errors:
            max_randons = meus_randons
        max_errors = max([max_errors, position]) 
    print("randons :", max_randons, "total :", total)
    print("Maximo de erros foi:", max_errors) 
  
  
    
def predicao(num_erros, d_n_dn=0):
    ini = time.time()
    
    if d_n_dn == 0:
        resultados = Resultado.objects.order_by('-data')[:num_erros]
    elif d_n_dn == 1:
        resultados = Resultado.objects.filter(turno=1).order_by('-data')[:num_erros]
    else:
        resultados = Resultado.objects.filter(turno=2).order_by('-data')[:num_erros]
    print(str(['data: %s turno: %s' % (str(r.data),str(r.turno)) for r in resultados]))
    resultados_grupos = constroi_cache(resultados)
    all_errors = False
    while not all_errors:
        # tenta errar num_erros
        all_errors = True
        cur_randons = []
        for resultado_grupo in resultados_grupos[::-1]:
            random_grupo = random.randint(1,25)
            cur_randons.append((random_grupo, resultado_grupo))
            if random_grupo in resultado_grupo:
                all_errors = False
                break
    print time.time() - ini
    return random.randint(1,25)   
    
import datetime
def copy():
    with open('/app/resultados/dados/db.csv', 'r') as f:
        for line in f:
            v = line.split(',')
            r = Resultado()
            r.data = datetime.date(*[int(s) for s in v[1].split('-')])
            r.turno = str(v[2])
            r.premio_1 = str(v[3])
            r.premio_2 = str(v[4])
            r.premio_3 = str(v[5])
            r.premio_4 = str(v[6])
            r.premio_5 = str(v[7])
            r.premio_6 = str(v[8])
            r.premio_7 = str(v[9])
            r.premio_8 = str(v[10])
            r.premio_9 = str(v[11])
            r.premio_10 = str(v[12])
            r.save()
    
