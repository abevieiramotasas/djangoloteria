from resultados.models import Resultado
import time
import random


def super_metodo(TIME_MAX):
    time_inicial = time.time()
    max_errors = 0

    # inicio com 40
    resultados = Resultado.objects.order_by('-data')[:60]

    def grupo(milhar):
        return (((int(milhar)-1)%100)/4)+1
        
    grupos_cache =  []

    def constroi_cache(res):
        for resultado in res:
            grupos_cache.append([grupo(milhar) for milhar in resultado.resultados()])

    constroi_cache(resultados)
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
            random_grupo = random.randint(0,24)           
            # verifico se o grupo randomizado saiu no resultado
            wrong_random = True  
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
    print("randons :", max_randons)
    print("Maximo de erros foi:", max_errors)   
        
        
