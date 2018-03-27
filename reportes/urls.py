from django.conf.urls import url
from reportes.views import index

urlpatterns = [
    url(r'^index$', index),
]
