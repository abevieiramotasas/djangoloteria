from django.contrib import admin
from models import Resultado

class ResultadoAdmin(admin.ModelAdmin):
	# informa os campos que sao apresentados na tela de listagem das entidades
	list_display = ('data', 'turno_s', 'premio_1','premio_2','premio_3','premio_4','premio_5','premio_6','premio_7','premio_8','premio_9','premio_10', )
	list_filter = ['data', 'turno',]
	search_fields = ['premio_1','premio_2','premio_3','premio_4','premio_5','premio_6','premio_7','premio_8','premio_9','premio_10',]
	date_hierarchy = 'data'
	actions_on_bottom = True
	actions_on_top = False
	list_per_page = 40
admin.site.register(Resultado, ResultadoAdmin)
