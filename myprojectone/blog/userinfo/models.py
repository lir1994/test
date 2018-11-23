from django.db import models

# Create your models here.

class ShowInfo(models.Model):
	nickname = models.CharField('昵称',max_length=20,null=True,default='我本无名')
	headimge = models.ImageField('头像',upload_to='static/images/headimage',default='normal.png')
	autograph = models.CharField('个性签名',max_length=200,null=True)

	def __str__(self):
		return self.nickname


	class Meta:
		db_table = 'showinfo'
		verbose_name = '展示信息'
		verbose_name_plural = verbose_name



class UserInfo(models.Model):
	name = models.CharField(verbose_name='用户名',max_length=50,null=False)
	password = models.CharField('密码',max_length=200,null=False)
	email = models.CharField('邮箱',max_length=100,null=False)
	phone = models.CharField('电话',max_length=20,null=False)
	time = models.DateTimeField('注册时间',auto_now=True)
	showuser = models.OneToOneField(ShowInfo)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'userinfo'
		verbose_name = '用户信息'
		verbose_name_plural = verbose_name


