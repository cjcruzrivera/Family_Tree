from django.conf.urls import url
from familia.views import index, new_familia, list_familia, edit_familia, delete_familia

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nueva$', new_familia, name='nueva_familia'),
    url(r'^listar$', list_familia, name='listar_familias'),
    url(r'^editar/(?P<id_familia>\d+)$', edit_familia, name='editar_familia'),
    url(r'^eliminar/(?P<id_familia>\d+)$', delete_familia, name='eliminar_familia'),
]
