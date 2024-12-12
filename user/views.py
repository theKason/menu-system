from django.shortcuts import render
from django.views import View
from user import models
from django.http import JsonResponse, HttpResponse

# Create your views here.
class userIndex(View):
    # 处理 GET 请求（获取用户信息）
    def get(self, reuqest):

        ID = reuqest.GET['id']
        try:
            # 根据 URL 的 id参数 获取用户id去数据库查询
            obj = models.User.objects.get(id=ID)
            return JsonResponse(obj)
        except:
            return HttpResponse('user does not exists')
        
    # 处理 POST 请求（新建用户）
    def post(self, request):
        pass

    # 处理 PUT 请求（更改用户）
    def put(self, request):
        pass

    # 处理 DELETE 请求（删除用户）
    def delete(self, request):
        pass