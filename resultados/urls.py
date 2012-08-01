from django.conf.urls import patterns, url


urlpatterns = patterns('resultados.views',
    # url(r'^download/$', 'download'),
    url(r'^(?P<num>\d+)/(?P<turno>\d)$', 'predizer'),
    url(r'^update/(?P<dia>\d{1,2})-(?P<mes>\d{1,2})-(?P<ano>\d{4})', 'atualiza'),
    url(r'^mais_velho/(?P<turno>\d)$', 'mais_velho'),
)
