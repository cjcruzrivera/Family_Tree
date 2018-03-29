from django.conf.urls import url
from persona.views import index, new_persona, list_persona

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nueva$', new_persona, name = "nueva_persona"),
    url(r'^listar$', list_persona, name = "listar_personas"),
]
