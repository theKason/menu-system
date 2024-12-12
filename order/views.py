from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from order import models
from user import models

# Create your views here.
class orderIndex(View):
    def get(self, request): 
        # GET请求 参数在url中，同过request 对象的 GET属性获取
        ID = request.GET['id']

        try:
            # 获取当前用户的所有订单记录（QuerySet对象）
            # 外键表反向访问
            # 1.先获取当前用户
            user = models.User.objects.get(id=ID)
            # 2.通过用户反向访问订单
            orders = user.order_set.all().values('order_status', 'time_crated', 'cuisine')

            return JsonResponse(list(orders))
        except:
            return HttpResponse('user does not own orders')
