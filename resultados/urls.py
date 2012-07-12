from django.conf.urls import patterns, url


urlpatterns = patterns('resultados.views',
    # url(r'^download/$', 'download'),
    url(r'^import/$', 'importcsv'),
)
