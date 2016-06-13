from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([0-9]+)/$', views.query_db),
    url(r'^$', views.insert_db),
]
