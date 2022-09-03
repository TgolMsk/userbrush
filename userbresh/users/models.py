from django.db import models
from django.contrib.auth.models import AbstractUser

#扩展默认用户模型
class UserAdd(AbstractUser):
	nick_name = models.CharField(max_length=50, verbose_name="别名")
	class Meta:
		verbose_name = "用户信息扩展"
		verbose_name_plural = verbose_name
			



#自定义用户模型
class UserConf(models.Model):
	#手机号
	user_phonenumber = models.CharField(max_length=16,verbose_name="手机号",unique=True)
	#头像
	user_img = models.ImageField(upload_to="head_image/%Y/%m",null=True,default="default.jpg",verbose_name="用户头像")
	#登陆密码
	user_password = models.CharField(max_length=24,verbose_name="登陆密码")
	#用户状态
	user_result = models.BooleanField(null=True,default=1,verbose_name="用户状态 True为允许登陆False为禁止登陆")
	#交易密码
	user_tc_password = models.CharField(max_length=6,verbose_name="6为交易密码")
	#昵称
	user_name = models.CharField(null=True,default="", max_length=12,verbose_name="用户名称")
	#会员等级
	user_vip = models.PositiveSmallIntegerField(null=True,default=0,verbose_name="会员VIP等级")
	#注册时间
	user_reg_time = models.DateTimeField(null=True,auto_now_add=True,verbose_name="注册时间" )
	#登陆时间
	user_login_time = models.DateTimeField(null=True,verbose_name="登陆时间" )
	#最后信息更改
	user_set_time = models.DateTimeField(null=True,auto_now=True,verbose_name="最后_更改时间")
	#注册ip地址
	user_ip = models.GenericIPAddressField(null=True,default="127.0.0.1",protocol="IPv4",verbose_name="用户注册ip地址")
	class Meta:
		verbose_name = "会员用户信息"
		verbose_name_plural = verbose_name
		db_table = 'user_conf'

