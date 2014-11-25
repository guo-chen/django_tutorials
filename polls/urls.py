from django.conf.urls import patterns, url
from polls import views


urlpatterns = patterns('',
                       url(r'^$', views.index2, name='index'),
                       url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
                       url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
                       )
