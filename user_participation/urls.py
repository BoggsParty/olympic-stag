from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'guess/(?P<sport>[\w-]+)', views.guess, name='guess'),
url(r'guesses/all/$', views.all_guess_one_user, name='all_guess_one_user'),
url(r'guesses/all/(?P<sport>[\w-]+)', views.all_guess_all_users, name='all_guess_all_users'),
url(r'message-board/$', views.messages_first_page, name='messages-first-page'),
url(r'message-board/(?P<num>[0-9]+)', views.messages, name='messages'),
url(r'message-board/comment/$', views.new_comment, name='new-comment'),
url(r'message-board/response/(?P<pk>[0-9]+)/$' , views.new_response, name='new-response'),
url(r'message-board/comment/edit/(?P<pk>[0-9]+)/$', views.edit_comment, name='edit-comment'),
url(r'message-board/response/edit/(?P<pk>[0-9]+)/$' , views.edit_response, name='edit-response'),
]