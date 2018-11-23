from django.db import models
from userinfo.models import ShowInfo,UserInfo
from blogapp.models import Blog
# Create your models here.

class Comment(models.Model):
	content = models.TextField('评论内容')
	ctime = models.DateTimeField('评论时间',auto_now=True)
	cblog = models.ForeignKey(Blog)
	cname = models.ForeignKey(UserInfo)

	def __str__(self):
		return self.content


	class Meta:
		db_table = 'comment'
		verbose_name = '评论'
		verbose_name_plural = verbose_name


class Reply(models.Model):
	rcontent = models.CharField('回复内容',max_length=300,null=False)
	rtime = models.DateTimeField('回复时间',auto_now=True)
	rcomment = models.ForeignKey(Comment)
	ruser = models.ForeignKey(UserInfo)

	def __str__(self):
		return self.rcontent


	class Meta:
		db_table = 'reply'
		verbose_name = '回复'
		verbose_name_plural = verbose_name


class Collection(models.Model):
	collorderNo = models.CharField(max_length=50) 
	colldetail = models.TextField('收藏详情')
	colltime = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(UserInfo)

	def __str__(self):
		return self.collorderNo


	class Meta:
		db_table = 'Collection'
		verbose_name = '收藏夹'
		verbose_name_plural = verbose_name



