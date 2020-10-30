from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,PropertyForm
from django.contrib.auth.forms import UserCreationForm
from .models import Property
# Create your views here.
def index(request):
    flatss=Property.objects.filter(propertytype='Flat')
    bungalowss=Property.objects.filter(propertytype='Bungalow')
    context={'flatss':flatss,'bungalowss':bungalowss}
    return render(request,'index.html',context)
  

def allproperty(request):
	Propertys=Property.objects.all()
	context={'Propertys':Propertys}
	return render(request,'propertys.html',context)

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


