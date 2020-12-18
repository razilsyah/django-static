from django.conf.urls import url

from . import views as viewsBlog
urlpatterns = [
    url(r'^$', viewsBlog.index)
]
