from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login),
    url(r'^register', views.register),
    url(r'^logout$', views.logout),
    url(r'^trabajador/(?P<pk>\d+)$', views.detail),
    url(r'^detail', views.detalle_trabajador),
]
