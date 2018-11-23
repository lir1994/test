from django.conf.urls import url
from django.contrib import admin
from userinfo import views

urlpatterns = [
	url('^register/$',views.register,name='register'),
	url('^register_in/$',views.register_in,name='register_in'),
	url('^checkname/$',views.check_username,name='checkname'),
	url('^checkpword/$',views.check_pword,name='checkpword'),
	url('^login/$',views.login,name='login'),
	url('^login_in/$',views.login_in,name='login_in'),
	url('^login_out/$',views.login_out,name='login_out'),
]