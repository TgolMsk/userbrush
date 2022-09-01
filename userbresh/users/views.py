from django.shortcuts import render
from users.models import UserConf

#用户登录
def user_login(request):
	return render(request,'login.html')
