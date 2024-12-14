from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from cuisine.models import Cuisine
import json

def getCategory(cur_category):
    # 获取当前分类的所有菜品（QuerySet对象）
    cuisineList = Cuisine.objects.filter(category=cur_category) # 一个分类含有多个菜品对象，必须用filter()方法处理！！！
    # 将对象所有属性序列化
    serialCuisineList = []
    for cuisine_obj in cuisineList:
        # 使用dict存储当前对象的信息
        data = {
            'id': cuisine_obj.id,
            'name': cuisine_obj.name,
            'desc': cuisine_obj.desc,
            'avatar': cuisine_obj.avatar.url, # 当序列化时，可以使用 image.url 获取图片的 URL
        }

        serialCuisineList.append(data)

    return serialCuisineList

# Create your views here.
class cuisineIndex(View):
    '''
    Django会根据请求方法自动调用类视图的对应函数
    '''
    # 处理 GET 请求（返回所有菜品（按照分类））
    def get(self, request):
        # 创建空字典存放菜品(按照分类)
        # 数据结构：{
        #           "Meat":[...], 
        #           "Vegetable":[...], 
        #           ...
        #          }
        cuisineDict = {}

        for sort in ["Meat", "Vegetable", "Dessert", "Beverage"]:
            sortList = getCategory(sort)
            cuisineDict[sort] = sortList

        # 返回Json对象
        return JsonResponse(cuisineDict, safe=False)
    
    # 处理 POST 请求（创建新菜品）   
    def post(self, request, *args, **kwargs):
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
        except:
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

        接收数据格式（例子）：
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
        
        # 根据菜品ID获取菜品对象
        try:
            to_update_cuisine = Cuisine.objects.get(id=params_data['id'])
            # 忽略不需要更改的参数
            for param, value in params_data.items(): # 同时获取字典的键和值，可以使用 .items() 方法。这将返回每一对键值元组
                if param == 'id' or value == None:
                    continue
                to_update_cuisine.__dict__[param] = value # __dict__ 是 Python 中所有对象都有的一个字典，它包含了对象的所有实例属性
                to_update_cuisine.save()
        except:
            return HttpResponse('所需数据缺少')
        else:
            return HttpResponse('菜品更改完成')

    # 处理 DELETE 请求（删除菜品）
    def delete(self, request):
        # 通过解析reuqest.body来获取菜品id
        cuisine_id = json.loads(request.body)['id']
        try:
            Cuisine.objects.filter(id=cuisine_id).delete()
        except:
            return HttpResponse('菜品删除失败')
        else:
            return HttpResponse('菜品删除成功')


