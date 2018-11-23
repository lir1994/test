from django.shortcuts import render
from blogapp.models import *
# Create your views here.
def index(request):
	classify = Classify.objects.all()
	print(classify)
	blog = Blog.objects.all()
	print(blog)

	return render(request,'index.html',{'blog_list':locals()})

def detail_one(request):
	blog_id = request.GET.get('goodid')[:-1]
	blog_one = Blog.objects.filter(id=blog_id)
	blogone = blog_one[0]
	return render(request,'detail.html',locals())