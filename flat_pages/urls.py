from django.conf.urls import include, url
from . import views

urlpatterns = [
#url(r'^about/$', views.about, name='about'),
url(r'^calendar/$', views.calendar, name='calendar'),
url(r'^(?P<slug>[\w-]+)/$', views.flat_page, name='flat_page'),
]