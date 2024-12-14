from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from order.models import Order, OrderCuisine 
from user.models import User
from cuisine.models import Cuisine
import json

# Create your views here.
class orderIndex(View):
    '''
    Django会根据请求方法自动调用类视图的对应函数
    '''
    def get(self, request): 
        '''
        返回数据结构：。。。
        '''
        try:
            # 获取当前用户的所有订单记录（一次性返回所有数据，不做二次查询）
            # ---外键表反向访问
            # 1.先获取当前用户
            user_id = request.GET.get('user_id') # 查询字符串参数
            user = User.objects.get(id=user_id)
            # 2.通过用户反向访问订单（QuerySet对象）
            orders = user.order_set.all()
            # 3.构建返回数据形式（需要的参数：status、time_created，cuisines）
            orders_list = []
            # 3.1构建每个订单
            for order in orders:
                temp_order_dict = {}
                temp_order_dict['id'] = order.id
                temp_order_dict['time_created'] = order.time_created
                #3.2构建每个订单的菜品
                cuisine_list = []
                cuisines = order.cuisines.all()# QuerySet对象
                for cuisine in cuisines:
                    temp_cuisine_dict = {}
                    temp_cuisine_dict['name'] = cuisine.name
                    temp_cuisine_dict['avatar'] = cuisine.avatar.url
                    cuisine_list.append(temp_cuisine_dict)

                temp_order_dict['cuisines'] = cuisine_list
                orders_list.append(temp_order_dict)

            return JsonResponse(orders_list, safe=False)
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('user does not own orders')
        
    def post(self, request):
        '''
        请求数据结构：
        {
            "status": "已完成",
            "user_id": 1,
            "cuisines": {
                "id1": amount1,
                "id2": amount2
            }
        }
        '''
        try:
            # 除 GET 外的请求方法参数可以请求体获得，但先要把数据通过json.loads()解析成python对象
            data = json.loads(request.body)
            obj_order_status = 1 if data.get('status') == '已完成' else 2
            obj_customer = data.get('user_id')
            cuisine_dict = data.get('cuisines')

            order_obj = Order.objects.create(
                status = obj_order_status,
                customer_id = obj_customer # 外键字段名 + "_id"  或者 传入外键对象实例
                )
            
            # 重新获取刚创建的订单（通过时间戳字段）
            order_obj = Order.objects.order_by('-time_created').first()# 降序排列

            # order_obj.cuisines.add(cuisine_queryset)
            # 如果你定义了一个自定义的中间表（通过 through 参数），则不能直接使用 add()，必须通过创建中间模型实例来关联

            for cuisine_id, cuisine_amount in cuisine_dict.items():
                cuisine_obj = Cuisine.objects.get(id=int(cuisine_id))
                OrderCuisine.objects.create(
                    order=order_obj, 
                    cuisine=cuisine_obj, 
                    amount=cuisine_amount
                    )

            # order_obj.save()
            # 使用 Model.objects.method() 时不需要显式调用 .save()
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('订单创建失败')
        else:
            return HttpResponse('订单创建成功')

    # 处理 DELETE 请求
    def delete(self, request): # 使用 kwargs 来动态接收多余的参数
        '''
        请求数据结构:
        {
            "order_id": int
        }
        '''
        try:
            # 通过订单ID来获取订单对象
            user_id = json.loads(request.body).get('user_id')
            Order.objects.filter(id=user_id).delete()
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('订单删除失败')
        else:
            return HttpResponse('订单删除成功')