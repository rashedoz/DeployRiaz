from django.views.generic import TemplateView
from django.shortcuts import render, redirect

# Create your views here.


class HomeView(TemplateView):
	print("called")
	template_name = 'home.html'

	def get(self,request):
		print("get home")
		#Check If anonymous user
		
		return render(request,self.template_name) 
