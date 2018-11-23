from django.conf.urls import url
from operate import views

urlpatterns = [
	url('^addcollect/',views.add_collection,name='add_collection'),
	url('^collect/',views.collect,name='collect'),
]