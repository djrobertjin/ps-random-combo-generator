from django.conf.urls import url

from . import views

app_name = 'randomGen'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^generate/$', views.generate, name='generate')

]