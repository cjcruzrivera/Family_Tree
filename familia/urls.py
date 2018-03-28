from django.conf.urls import url
from familia.views import index

urlpatterns = [
    url(r'^index$', index),
    url(r'^$', index),
]
