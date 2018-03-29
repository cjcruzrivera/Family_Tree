from django.conf.urls import url
from reportes.views import index_reportes

urlpatterns = [
    url(r'^$', index_reportes),
]
