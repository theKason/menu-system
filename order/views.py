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
        请求数据结构（参数放在url）:
        {"user_id": int}

        返回数据结构:
        [
            {
                "id": 24,
                "time_created": "2024-12-14T11:28:52.490Z",
                "cuisines": [
                    {
                        "name": "小炒黄牛肉",
                        "avatar": "/media/%E5%B0%8F%E7%82%92%E9%BB%84%E7%89%9B%E8%82%89.jpeg"
                    },
                    {
                        "name": "麻婆豆腐",
                        "avatar": "/media/%E9%BA%BB%E5%A9%86%E8%B1%86%E8%85%90.jpeg"
                    },
                    {
                        "name": "上汤豆苗",
                        "avatar": "/media/%E4%B8%8A%E6%B1%A4%E8%B1%86%E8%8B%97.jpeg"
                    }
                ]
            },
            {
                "id": 25,
                ...
            }
        ]
        '''
        try:
            # 获取当前用户的所有订单记录（一次性返回所有数据，不做二次查询）
            # ---外键表反向访问

            # 1.先获取当前用户
            user_id = request.GET.get('user_id') # 查询字符串参数
            user = User.objects.get(id=user_id)

            # 2.通过用户反向访问订单（QuerySet对象）
            orders = user.order_set.all() # 这里可以直接使用 user.order_set.all().values('name','avatar')来获取目标参数

            # 3.构建返回数据形式（需要的参数：status、time_created，cuisines）
            orders_list = []
            for order in orders: # 3.1构建每个订单
                temp_order_dict = {}
                temp_order_dict['id'] = order.id
                temp_order_dict['time_created'] = order.time_created
                
                cuisine_list = []
                cuisines = order.cuisines.all()# QuerySet对象
                for cuisine in cuisines: # 3.2构建每个订单的菜品
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
        请求数据结构（参数放在请求体）：
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
        请求数据结构（参数放在请求体）:
        {
            "order_id": int
        }
        '''
        try:
            # 通过订单ID来获取订单对象
            user_id = json.loads(request.body).get('order_id')
            Order.objects.filter(id=user_id).delete()
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('订单删除失败')
        else:
            return HttpResponse('订单删除成功')