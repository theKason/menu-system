from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from order.models import Order
from user.models import User
from cuisine.models import Cuisine

# Create your views here.
class orderIndex(View):
    '''
    Django会根据请求方法自动调用类视图的对应函数
    '''
    
    def get(self, request): 
        # GET请求 参数在url中，同过request 对象的 GET属性获取
        ID = request.GET['user_id']

        try:
            # 获取当前用户的所有订单记录（QuerySet对象）
            # 外键表反向访问
            # 1.先获取当前用户
            user = User.objects.get(id=ID)
            # 2.通过用户反向访问订单
            orders = user.order_set.all().values('order_status', 'time_created', 'cuisine')

            return JsonResponse(list(orders))
        except:
            return HttpResponse('user does not own orders')
        
    def post(self, request, *args, **kwargs): # 使用 kwargs 来动态接收多余的参数
        # POST请求 参数在request.POST中，同过request.POST.get(<属性名>)获取
        obj_order_status = '已完成' if request.POST.get('order_status') == 1 else '未完成'
        obj_customer = request.POST.get('customer_id')

        # 先通过 订单状态 和 用户ID 来创建订单
        order_obj = Order.objects.create(
            order_status = obj_order_status,
            customer = obj_customer
            )
        
        # 获取所有菜品ID
        cuisine_id_list = request.POST.get('cuisines')

        # 通过ID获取所有cuisine的实例对象
        cuisine_objs = []
        for cuisine_id in cuisine_id_list:
            cuisine = Cuisine.objects.get(id=cuisine_id)
            cuisine_objs.append(cuisine)

        # 将菜品列表一次传入当前订单对像
        order_obj.cuisines.add(cuisine_objs)

    # 处理 DELETE 请求
    def delete(self, request, *args, **kwargs): # 使用 kwargs 来动态接收多余的参数
        # 通过订单ID来获取订单对象
        Order.objects.filter(request.DELETE.get('order_id')).delete()
