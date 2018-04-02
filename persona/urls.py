from django.conf.urls import url
from persona.views import index, new_persona, list_persona, edit_persona, delete_persona

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nueva$', new_persona, name = "nueva_persona"),
    url(r'^listar$', list_persona, name = "listar_personas"),
    url(r'^editar/(?P<id_persona>\d+)$', edit_persona, name='editar_persona'),    
    url(r'^eliminar/(?P<id_persona>\d+)$', delete_persona, name='borrar_persona'),    
]
