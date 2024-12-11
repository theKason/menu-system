from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from models import *

# Create your views here.
class orderIndex(View):
    def get(self, request): 
        # GET请求 参数在url中，同过request 对象的 GET属性获取
        id = request.GET['id']

        # 获取当前用户的所有订单记录（QuerySet对象）
        qs = Order.objects.filter(
            customer=id).values(
                'order_status', 'time_crated', 'cuisine')

        return JsonResponse(list(qs))
