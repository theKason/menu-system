from django.db import models

# Create your models here.
class Cuisine(models.Model):
    # 菜的名称
    name = models.CharField(max_length=20, unique=True)
    # 菜的价格
    price = models.IntegerField()
    # 菜的描述
    desc = models.TextField(null=True, blank=True)
    # 菜的图片
    avatar = models.ImageField(null=True, blank=True)
    # 菜的类别：这里使用 enumeration classes 来定义菜的类别
    cuisine_type = models.TextChoices("Meat","Vegetable","Dessert","Beverage")
        
