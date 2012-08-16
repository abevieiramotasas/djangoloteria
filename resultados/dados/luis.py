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
        
def gera_array(r):
    resultado = [r.premio_1,r.premio_2,r.premio_3,r.premio_4,r.premio_5,r.premio_6,r.premio_7,r.premio_8,r.premio_9,r.premio_10]
    return [int(r) for r in resultado]        

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
            r.premio_10 = str(v[12][:4])
            r.save()

def more(badge, base, t):
    if (badge is None or len(badge) is 0):
        base = base + 10
        if (int(t) is 0):
            badge = Resultado.objects.order_by('-data', 'turno')[base - 10:base]
        else:            
            badge = Resultado.objects.filter(turno=t).order_by('-data')[base - 10:base]
        badge = [r for r in badge]
    resultado = badge[0]
    del(badge[0])
    return (resultado, badge, base)        
        
def mais_velho(turno=0):
    i = 0
    premios = [[] for _ in range(10)]
    badge = None
    base = 0
    while (i < 250):
        r, badge, base = more(badge, base, turno)
        # meu deus, porque nao fui atras de ver como usar array com o orm
        p = grupo(r.premio_1)
        # print(str(badge))
        if (not p in [x for x,y,z in premios[0]]):
            premios[0].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_2)
        if (not p in [x for x,y,z in premios[1]]):
            premios[1].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_3)
        if (not p in [x for x,y,z in premios[2]]):
            premios[2].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_4)
        if (not p in [x for x,y,z in premios[3]]):
            premios[3].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_5)
        if (not p in [x for x,y,z in premios[4]]):
            premios[4].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_6)
        if (not p in [x for x,y,z in premios[5]]):
            premios[5].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_7)
        if (not p in [x for x,y,z in premios[6]]):
            premios[6].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_8)
        if (not p in [x for x,y,z in premios[7]]):
            premios[7].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_9)
        if (not p in [x for x,y,z in premios[8]]):
            premios[8].append((p, r.data, r.turno))
            i = i + 1
        p = grupo(r.premio_10)
        if (not p in [x for x,y,z in premios[9]]):
            premios[9].append((p, r.data, r.turno))
            i = i + 1
    return premios   
    
def gera_formatado_all(a,b,c):
    t = {u'1':'Noturno', u'2':'Diurno'}
    table = """
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <table border="0">
    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    """
    values = [[] for _ in range(30)]
    pos = 0
    for x in range(10):
        for z in [a,b,c]:
            values[pos].append('<table border="1" cellspacing="2" cellpadding="5">')            
            values[pos].append('<b>premio %d</b>' % (x + 1))
            for grupo, data, turno in z[x][::-1]:
                values[pos].append('<tr><td>')               
                values[pos].append('<b>%d</b></td><td>%s</td><td>%s' % (grupo, data.strftime('%d/%m/%y'), t[turno]))                
                values[pos].append('</td></tr>')
            values[pos].append('</table>')
            pos = pos + 1
    print([''.join(v) for v in values][0])
    return table % tuple([''.join(v) for v in values])
    
    
def gera_formatado(a, nome):
    t = {u'1':'Noturno', u'2':'Diurno'}
    table = """
    <table border="1">

    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td>%s</td><td>%s</td></tr>

    </table>"""
    values = [[] for _ in range(10)]
    i = 1
    for a_r in a:
        values[i-1].append('<table border="1" cellspacing="2" cellpadding="5">')
        values[i-1].append('%d' % i)
        for grupo, data, turno in a_r[::-1]: 
            values[i-1].append('<tr><td>')               
            values[i-1].append('%d</td><td>%s</td><td>%s' % (grupo, data.strftime('%d/%m/%y'), t[turno]))                
            values[i-1].append('</td></tr>')
        i = i + 1
        values[i-2].append('</table>')
    return table % tuple([''.join(v) for v in values])
    
    
def results_pos(turn):
    final = [[[] for _ in range(25)] for _ in range(10)]
    t = 0
    rr = Resultado.objects.filter(turno=turn).order_by('-data')
    for r in rr:
        l = gera_array(r)
        for i in range(10):
            r_i = l[i]
            final[i][grupo(r_i) - 1].append(t)
        t = t+1
    return final
