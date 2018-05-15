from django.urls import path
from . import views
from home.views import HomeView


urlpatterns=[
	# /home/

	path('',HomeView.as_view(),name='home'),


]