from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from cuisine.models import Cuisine

def getCategory(category):
    # 获取当前分类的所有菜品（QuerySet对象）
    cuisineList = Cuisine.objects.get(cuisine_type=category)
    return list(cuisineList)

# Create your views here.
class cuisineIndex(View):
    # 处理 GET 请求（返回所有菜品（按照分类））
    def get(self, request):
        # 创建空字典存放菜品(按照分类)
        cuisineList = {}

        for sort in ["Meat", "Vegetable", "Dessert", "Beverage"]:
            sortList = getCategory(sort)
            cuisineList[sort] = sortList

        # 返回Json对象
        return JsonResponse(cuisineList)
    
    # 处理 POST 请求（创建新菜品）   
    def post(self, request):
        # 获取所有菜品属性
        try:
            obj_name = request.POST.get('name')
            obj_price = request.POST.get('price')
            obj_desc = request.POST.get('price')
            obj_avatar = request.POST.get('avatar')
            obj_category = request.POST.get('category')
        except:
            return HttpResponse('所需数据缺失')

        cuisine_obj = Cuisine.objects.create(
            name = obj_name,
            price = obj_price,
            desc = obj_desc,
            avatar = obj_avatar,
            category = obj_category
        )

        cuisine_obj.save()

    # 处理 PUT 请求（编辑菜品）
    def put(self, request):
        try:
            obj_name = request.PUT.get('name')
            obj_price = request.PUT.get('price')
            obj_desc = request.PUT.get('price')
            obj_avatar = request.PUT.get('avatar')
            obj_category = request.PUT.get('category')
        except:
            return HttpResponse('所需数据确实')
        
        # 根据菜品ID获取菜品对象
        Cuisine.objects.filter(id=request.PUT.get('cuisine_id')).cuisine.objects.update(
            name = obj_name,
            price = obj_price,
            desc = obj_desc,
            avatar = obj_avatar,
            category = obj_category
        )

    # 处理 DELETE 请求（删除菜品）
    def delete(self, request):
        Cuisine.objects.filter(id=request.PUT.get('cuisine_id')).delete()



