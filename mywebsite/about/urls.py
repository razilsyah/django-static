from django.conf.urls import url

from . import views as viewsAbout

urlpatterns = [
    url(r'^$', viewsAbout.index),
]
