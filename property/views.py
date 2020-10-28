from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,PropertyForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form=SignUpForm()

	return render(request,'signup.html',{'form':form})


def addproperty(request):
	if request.method=='POST':
		form=PropertyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form=PropertyForm()

	return render(request,'addproperty.html',{'form':form})


