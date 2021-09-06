from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#user = User.objects.create_user('fake', 'lennon@thebeatles.com', 'fake')
#user.save()

#user = authenticate(username='john', password='secret')
#print(f"Hello, \'{name}\'")

def main(request):
	return	render(request, 'index.html')

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	if request.method == 'POST':
		name1 = request.POST.get('user')
		passw1 = request.POST.get('password')
		email = 'abc@gmail.com'
		#name1 = 'password'
		#passw1 = 'password'
		#user = User.objects.create_user(f"\'{name1}',\'{email}\',\'{passw1}\'")
		#user = User.objects.create_user(f"\'{name1}',"f"\'{email}',"f"\'{passw1}'")
		user = User(username=f'{name1}')
		user.set_password(f'{passw1}')
		#user.email(f'{email}')
		user.save()
		return HttpResponse('registered successfully')



def perfect(request):
	name = request.POST.get('user')
	passw = request.POST.get('password')
	#name = 'hello'
	#passw = 'hello'
	#user = authenticate(f"username = \'{name}',password = \'{passw}\'")
	#user = authenticate(username='fake', password='hello')
	user = authenticate(request,username=name,password=passw)
	if user is not None:
		#return HttpResponse(f"\'{name}',\'{passw}\'")
		return HttpResponse('login successfully')
	else:
		return HttpResponse('login failled')
