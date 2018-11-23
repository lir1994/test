from django.shortcuts import render
from userinfo.models import UserInfo
from .models import *
import json
from django.http import HttpResponse
import datetime
import json

# Create your views here.

def add_collection(request):
	blog_ti = request.POST.get('title')
	blog_con = request.POST.get('content')
	blog_au = request.POST.get('author')
	blog_pub = request.POST.get('pubtime')
	user_id = request.session.get('user_id')
	user = UserInfo.objects.get(id=user_id)
	print('*************')
	print(blog_ti)
	print(blog_con)
	print(blog_au)
	print(blog_pub)
	print(user)


	colldet = {"title":blog_ti,"content":blog_con,"author":blog_au,"pubtime":blog_pub}
	print('1--->',colldet["title"])
	print('2---->',colldet["content"])
	colldetail = json.dumps(colldet)
	print('3--->',type(colldet))
	print('4---->',type(colldetail))
	print('5---->',colldetail)
	collorderNo = datetime.datetime.now().strftime('%H%M%S%f')
	collection = Collection.objects.create(collorderNo=collorderNo,
		colldetail=colldetail,user=user)
	date = {"static":"OK"}
	return 	HttpResponse(json.dumps(date))
	# return render(request,'collect.html',locals())

def collect(request):
	user_id = request.session.get('user_id')
	print(user_id)
	coll = Collection.objects.filter(user=user_id)
	jsonobj = coll[0].colldetail

	dic = json.loads(jsonobj)
	
	# l = []
	# for val in dic.values():
	# 	l.append(val)
	# print(val)

	return render(request,'collect.html',locals())