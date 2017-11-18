from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='course_list'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail), #we put this first bcoz
    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
