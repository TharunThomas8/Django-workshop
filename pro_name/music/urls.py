from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^list/$', views.music, name = 'music'),
	url(r'^(?P<pk>[0-9]+)/$',viwes.listsong, name="list_song"),
]
