from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([ \w]+)', views.send_data),
    url(r'^$', views.index, name='index'),
]
