from django.shortcuts import render,redirect
from .models import UserInfo
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
import json
from django.db import DataError,DatabaseError

# Create your views here.

def register(request):
	return render(request,'register.html')

def register_in(request):
	new_user = UserInfo() 
	new_user.name = request.POST.get('username')
	user = UserInfo.objects.filter(name=new_user.name)
	print(user)
	if len(user) > 0:
		return render(request,'register.html',{"massage":"用户名已存在"})
	password = request.POST.get('password')
	spassword = request.POST.get('spassword')
	if password != spassword:
		return render(request,"register.html",{"massage":"两次密码不一致"})
	new_user.password = make_password(password,'abc','pbkdf2_sha256') 
	new_user.email = request.POST.get('email')
	new_user.phone = request.POST.get('phone')
	new_user.save()
	return render(request,'register.html')

def check_username(request):
	if request.is_ajax():
		new_user = UserInfo()
		new_user.name = request.POST.get('username')
		user = UserInfo.objects.filter(name=new_user.name)

		if len(user) > 0:
			msg = {'message':'该用户已存在'}
			data = json.dumps(msg)
			print('wo shi data',data)
			return HttpResponse(data,content_type='application/json')
		else:
			msg = {'message':'该用户名可以使用'}
			data = json.dumps(msg)
			print('wo shi data',data)
			return HttpResponse(data,content_type='application/json')
		
		

def check_pword(request):
	if request.is_ajax():
		if request.POST.get('password') != request.POST.get('spassword'):
			msg ={'message1':'两次输入密码不一致'}
			data = json.dumps(msg)
			print('wo shi data',data)
			return HttpResponse(data,content_type='application/json')
		else:
			msg ={'message1':'两次输入密码一致'}
			data = json.dumps(msg)
			print('wo shi data',data)
			return HttpResponse(data,content_type='application/json')


def login(request):
	return render(request,'login.html')

def login_in(request):
	if request.method == 'POST':
		user = UserInfo()
		user.name = request.POST.get('username')
		user.password = request.POST.get('password')
		try:
			users = UserInfo.objects.filter(name=user.name)
			print(users)
			if len(users) <= 0:
				return render(request,'login.html',{"message":"用户名不存在"})
			if not check_password(user.password,users[0].password):
				return render(request,'login.html',{"message":"用户名或密码错误"})
		except DatabaseError as e:
			logging.warning(e)
		request.session['user_id'] = users[0].id
		request.session['user_name'] = users[0].name
		# return render(request,'index.html')
		return redirect('/')
	return redirect('/user/login')
def login_out(request):
	if request.session['user_name']:
		del request.session['user_name']
		del request.session['user_id']
		return redirect('index')




