from django.db import models
from userinfo.models import ShowInfo,UserInfo
# Create your models here.



class Classify(models.Model):
	cname = models.CharField('类别',max_length=30,null=False)

	def __str__(self):
		return self.cname

	class Meta:
		db_table = 'classify'
		verbose_name = '类别'
		verbose_name_plural = verbose_name

class Tag(models.Model):
	tname = models.CharField('标签名',max_length=30,null=False)

	def __str__(self):
		return self.tname

	class Meta:
		db_table = 'tag'
		verbose_name = '标签'
		verbose_name_plural = verbose_name


class Blog(models.Model):
	title = models.CharField('标题',max_length=50,null=False)
	content = models.TextField('内容',null=False)
	pubtime = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(UserInfo)
	types = models.ForeignKey(Classify)
	btag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'blog'
		verbose_name = '博客'
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		if self.types.cname == '日常生活':
			return '/detail/?goodid={}/'.format(self.id)
		if self.types.cname == '智能科技':
			return '/detail/?goodid={}/'.format(self.id)

