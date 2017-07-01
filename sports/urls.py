from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'all/$', views.sport_menu, name='sport-menu'),
url(r'detail/(?P<sport>[\w-]+)', views.sport_detail, name='sport-detail'),
]