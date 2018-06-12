from django.conf.urls import url
from . import views
from django.contrib.auth import views as authViews
urlpatterns=[
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^login/$',authViews.login,{'template_name':'us_au/login.html'}),
	url(r'^logout/$',authViews.logout,{'template_name':'us_au/logout.html'})
]
