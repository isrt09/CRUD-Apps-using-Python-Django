from django.shortcuts import render

# Create your views here.

def home(request):
	template ='first_app/index.html'
	context = {}
	return render(request, template,context)

def student_form(request):
	template ='first_app/student_form.html'
	context = {}
	return render(request, template,context)
