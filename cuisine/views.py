from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from cuisine.models import Cuisine, Category
from order.models import OrderCuisine
import json

def getSaleNum(cuisine_obj):
    cuisineQuerySet = OrderCuisine.objects.filter(cuisine=cuisine_obj) # QuerySet对象
    num = 0 # 初始化销量总数
    for cuisine in  cuisineQuerySet:
        num += cuisine.amount
    return num


def getCategory(cur_category):
    # 获取分类实例对象
    category = Category.objects.get(name=cur_category)
    # 获取当前分类的ID
    ID = category.id
    # 获取当前分类的所有菜品（QuerySet对象）
    cuisineList = category.cuisine_set.all()
    # 将对象所有属性序列化
    serialCuisineList = []
    for cuisine_obj in cuisineList:
        # 使用dict存储当前对象的信息
        data = {
            'id': cuisine_obj.id,
            'name': cuisine_obj.name,
            'price': cuisine_obj.price,
            'sales': getSaleNum(cuisine_obj),
            'desc': cuisine_obj.desc,
            'avatar': cuisine_obj.avatar.url, # 用 image.url 获取图片的 URL 文本
        }

        serialCuisineList.append(data)

    categoryDict = {
        'id': ID,
        'name': cur_category,
        'dishes': serialCuisineList
        }

    return categoryDict

# Create your views here.
class cuisineIndex(View):
    '''
    Django会根据请求方法自动调用类视图的对应函数
    '''
    # 处理 GET 请求（返回所有菜品（按照分类））
    def get(self, request):
        '''
        返回数据结构:
        [
            {id: int,
            name: "肉"，
            dishes: [
                {
                    "id": 1,
                    "name": str,
                    "desc": str,
                    "avatar": "/media/%E5%B0%8F%E7%82%92%E9%BB%84%E7%89%9B%E8%82%89.jpeg"
                },
                {
                    "id": 2,
                    "name": str,
                    "desc": str,
                    "avatar": "/media/%E9%BA%BB%E5%A9%86%E8%B1%86%E8%85%90.jpeg"
                },
            ]},
            ...
        ]
        '''
        
        # 创建空列表存放菜品(按照分类)
        cuisineList = []

        try:
            cuisine_name = request.GET.get("cuisine_name")
            if cuisine_name == None:
                raise ValueError # 任意异常
        except: # 不是搜索请求
            for sort in ["肉", "菜", "甜品", "饮料"]: # 菜品分类写死，后续有更改这个列表需要同步更新！！！
                sortDict = getCategory(sort)
                cuisineList.append(sortDict)
            # 返回Json对象
            return JsonResponse(cuisineList, safe=False)
        else: # 搜索请求
            cuisineList = Cuisine.objects.filter(name__icontains=cuisine_name) # 模糊匹配
            cuisineList = cuisineList.values("id", "name", "avatar")
            return JsonResponse(list(cuisineList), safe=False)
    
    # 处理 POST 请求（创建新菜品）   
    def post(self, request):
        '''
        请求数据结构（参数放在表单）:
        {
            "name": str,
            "price": int,
            "desc": str,
            "avatar": url(str),
            "category": str
        }
        '''
        
        # 获取所有菜品属性
        obj_name = request.POST.get('name')
        obj_price = request.POST.get('price')
        obj_desc = request.POST.get('desc')
        obj_avatar = request.FILES.get('avatar')
        obj_category = request.POST.get('category')

        try:
            cuisine_obj = Cuisine.objects.create(
                name = obj_name,
                price = obj_price,
                desc = obj_desc,
                avatar = obj_avatar,
                category = obj_category
            )
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('所需数据缺少')
        else:
            cuisine_obj.save()
            return HttpResponse('菜品创建成功')
            

    # 处理 PUT 请求（编辑菜品）
    def put(self, request):
        '''
        Django 的默认请求对象（request）只会提供 GET 和 POST 属性，
        而不会直接提供 PUT、DELETE 等方法的请求数据。
        要处理 PUT 请求数据，需要使用 request.body 来获取原始请求数据，然后手动解析它。
        常见的做法是使用 json.loads 解析 JSON 数据，或者使用 django.http.QueryDict 来处理表单数据。

        请求数据结构（参数放在请求体）:
        {
            "id": int,
            "name": str,
            "price": int,
            "desc": str,
            "avatar": url(str),
            "category": str
        }

        返回数据结构:
        {
            "id": 19,
            "name": null,
            "price": 25,
            "desc":null,
            "avatar": null,
            "category": null 
        }
        '''

        params_data = json.loads(request.body.decode('utf-8'))
        
        try:
            # 根据菜品ID获取菜品对象
            to_update_cuisine = Cuisine.objects.get(id=params_data['id'])
            # 忽略不需要更改的参数
            for param, value in params_data.items(): # 同时获取字典的键和值，可以使用 .items() 方法。这将返回每一对键值元组
                if param == 'id' or value == None:
                    continue
                to_update_cuisine.__dict__[param] = value # __dict__ 是所有 Django model 对象都有的一个字典，包含了对象的所有实例属性
                to_update_cuisine.save()

        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('所需数据缺少')
        else:
            return HttpResponse('菜品更改完成')

    # 处理 DELETE 请求（删除菜品）
    def delete(self, request):
        '''
        请求数据结构（参数放在请求体）:
        {
            "id": [int, int, int]
        }
        '''

        # 通过解析reuqest.body来获取菜品id
        cuisine_id_list = json.loads(request.body)['id']
        try:
            Cuisine.objects.filter(id__in=cuisine_id_list).delete()
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('菜品删除失败')
        else:
            return HttpResponse('菜品删除成功')


