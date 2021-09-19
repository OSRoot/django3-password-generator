from django.shortcuts import render
from django.http import HttpResponse as HR
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html') 

def password(request):

	characters = list('abcdefghijklmnopqrstuvwxyz')

	length = int(request.GET.get('length'))
	
	thepassword = ''
	
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPRSTUVWXYZ'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*({"?>:<<~'))

	for x in range(length):
		thepassword += random.choice(characters)



	return render(request, 'generator/password.html', {'password':thepassword})

def about(request):

	return render(request, 'generator/about.html')