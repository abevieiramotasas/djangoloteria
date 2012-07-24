from dados import luis, crawler
from django.http import HttpResponse

def predizer(request, num, turno):
    # num = request.GET['num']
    return HttpResponse(str(luis.predicao(num, turno)))
    
def atualiza(request, dia, mes, ano):
    crawler.craw('%s/%s/%s' % (dia, mes, ano))
    return HttpResponse('Atualizado')
