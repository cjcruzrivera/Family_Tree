from django.conf.urls import url
from persona.views import index

urlpatterns = [
    url(r'^$', index),
]
