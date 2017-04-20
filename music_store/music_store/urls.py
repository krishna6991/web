from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),  #r representes regular expressiom
    url(r'^music/', include('music.urls')),
]
