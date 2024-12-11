from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from cuisine import models

def getCategory(category):
    # 获取当前分类的所有菜品（QuerySet对象）
    cuisineList = models.Cuisine.objects.get(cuisine_type=category)
    return list(cuisineList)

# Create your views here.
class cuisineIndex(View):
    def get(self, request):
        # 创建空字典存放菜品
        cuisineList = {}

        for c in ["Meat","Vegetable","Dessert","Beverage"]:
            temp = getCategory(c)
            cuisineList[c] = temp

        # 返回Json对象
        return JsonResponse(cuisineList)
