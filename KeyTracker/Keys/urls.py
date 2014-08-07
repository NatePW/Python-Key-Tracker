from django.conf.urls import patterns, url

from Keys import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)