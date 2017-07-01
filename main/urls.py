from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
urlpatterns = [
url(r'^$', views.main, name='main'),
url(r'^log-out/$', views.log_out, name='log-out'),
url(r'^user/settings/$', views.edit_settings, name='edit-settings'),
url('^create-account/', CreateView.as_view(
        template_name='registration/createaccount.html',
        form_class=UserCreationForm,
        success_url='/user/settings/'
    )),
]