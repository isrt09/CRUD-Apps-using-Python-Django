from django.shortcuts import render
from first_app import forms

# Create your views here.

def home(request):
	template ='first_app/index.html'
	context = {
		'title' :"Home"
	}
	return render(request, template,context)

def student_form(request):
	form = forms.StudentForm()
	if request.method == 'POST':
		form = forms.StudentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return home(request)
	template ='first_app/student_form.html'
	context = {
		'title' :"Student Form",
		'form':form
	}
	return render(request, template,context)
