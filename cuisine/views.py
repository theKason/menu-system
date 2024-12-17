from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from cuisine.models import Cuisine, Category
from order.models import OrderCuisine
import json

def getSaleNum(cuisine_obj):
   cuisineQuerySet = OrderCuisine.objects.filter(cuisine=cuisine_obj)
   num = 0
   for cuisine in cuisineQuerySet:
       num += cuisine.amount
   return num

def getCategory(cur_category):
   try:
       # 获取分类实例对象
       category = Category.objects.get(name=cur_category)
       # 获取当前分类的ID
       ID = category.id
       # 获取当前分类的所有菜品
       cuisineList = category.cuisine_set.all()
       # 将对象所有属性序列化
       serialCuisineList = []
       for cuisine_obj in cuisineList:
           data = {
               'id': cuisine_obj.id,
               'name': cuisine_obj.name,
               'price': cuisine_obj.price,
               'sales': getSaleNum(cuisine_obj),
               'desc': cuisine_obj.desc,
               'avatar': cuisine_obj.avatar.url,
           }
           serialCuisineList.append(data)

       categoryDict = {
           'id': ID,  
           'name': cur_category,
           'dishes': serialCuisineList
       }
       return categoryDict
   except Exception as e:
       print(f"Error in getCategory: {e}")
       return None

class cuisineIndex(View):
   def get(self, request):
       # 创建空列表存放菜品(按照分类)
       cuisineList = []

       try:
           cuisine_name = request.GET.get("cuisine_name")
           if cuisine_name == None:
               # 获取所有分类
               categories = Category.objects.all()
               for category in categories:
                   sortDict = getCategory(category.name)
                   if sortDict:  # 只添加成功获取的分类
                       cuisineList.append(sortDict)
               return JsonResponse(cuisineList, safe=False)
           else: # 搜索请求
               cuisineList = Cuisine.objects.filter(name__icontains=cuisine_name)
               cuisineList = cuisineList.values("id", "name", "avatar")
               return JsonResponse(list(cuisineList), safe=False)
       except Exception as e:
           return JsonResponse({
               'code': 500,
               'msg': str(e),
               'data': None
           })

   def post(self, request):
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

   def put(self, request):
       params_data = json.loads(request.body.decode('utf-8'))
       
       try:
           to_update_cuisine = Cuisine.objects.get(id=params_data['id'])
           for param, value in params_data.items():
               if param == 'id' or value == None:
                   continue
               to_update_cuisine.__dict__[param] = value
               to_update_cuisine.save()
       except Exception as e:
           print(f"Error: {e}")
           return HttpResponse('所需数据缺少')
       else:
           return HttpResponse('菜品更改完成')

   def delete(self, request):
       try:
           cuisine_id_list = json.loads(request.body)['id']
           Cuisine.objects.filter(id__in=cuisine_id_list).delete()
       except Exception as e:
           print(f"Error: {e}")
           return HttpResponse('菜品删除失败')
       else:
           return HttpResponse('菜品删除成功')