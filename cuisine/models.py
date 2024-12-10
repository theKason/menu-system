from django.db import models

# Create your models here.
class Category(models.Model):
    # 菜的类别
    name = models.CharField(max_length=5)

class Cuisine(models.Model):
    # 菜的名称
    name = models.CharField(max_length=20)
    # 菜的价格
    price = models.IntegerField()
    # 菜的描述
    desc = models.TextField()
    # 菜的图片
    # 菜的归类
    category = models.ForeignKey(Category, on_delete=models.CASCADE)