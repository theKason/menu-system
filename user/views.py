from django.shortcuts import render
from django.views import View
from user import models
from django.http import JsonResponse, HttpResponse

# Create your views here.
class userIndex(View):
    def get(self, reuqest):

        ID = reuqest.GET['id']
        try:
            # 根据 URL 的 id参数 获取用户id去数据库查询
            obj = models.User.objects.get(id=ID)
            return JsonResponse(obj)
        except:
            return HttpResponse('user does not exists')