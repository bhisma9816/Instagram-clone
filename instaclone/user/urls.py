from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.signin, name = "signin"),
	url(r'^signup/$', views.signup, name = "signup"),
]