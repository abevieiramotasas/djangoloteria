from dados import luis, crawler
from django.http import HttpResponse

def predizer(request, num, turno):
    # num = request.GET['num']
    return HttpResponse(str(luis.predicao(num, turno)))
    
def atualiza(request, dia, mes, ano):
    crawler.craw('%s/%s/%s' % (dia, mes, ano))
    return HttpResponse('Atualizado')

def atualiza_hoje(request):
    import datetime
    d = datetime.date.today()
    crawler.craw('%s/%s/%s' %(d.day, d.month, d.year))
    return HttpResponse('Atualizado')
    
def mais_velho(request, turno):
    return HttpResponse(luis.gera_formatado(luis.mais_velho(turno), ''), turno)
    
def index(request):
    html = """
    <a href='/loteria/35/0'>Predizer diurno e noturno</a><br>
    <a href='/loteria/35/2'>Predizer diurno</a><br>
    <a href='/loteria/35/1'>Predizer noturno</a><br>
    <a href='/loteria/update/'>Update(data no formato dd-mm-yyyy)</a><br>
    <a href='/loteria/mais_velho/0'>Mais velho diurno e noturno</a><br>
    <a href='/loteria/mais_velho/2'>Mais velho diurno</a><br>
    <a href='/loteria/mais_velho/1'>Mais velho noturno</a><br>
    """
    return HttpResponse(html)
