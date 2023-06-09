from django.urls import path, re_path
from . import views


urlpatterns = [
	path("", views.home, name='home'),
	path("detail/<slug:slug>/", views.detail, name='detail')
]