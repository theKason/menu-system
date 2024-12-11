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
        # 创建空字典存放菜品(按照分类)
        cuisineList = {}

        for sort in ["Meat", "Vegetable", "Dessert", "Beverage"]:
            sortList = getCategory(sort)
            cuisineList[sort] = sortList

        # 返回Json对象
        return JsonResponse(cuisineList)
