from django.db import models

# Create your models here.
class Cuisine(models.Model):
    # 菜的名称
    name = models.CharField(max_length=20, unique=True) # CharField 必须要有max_length属性
    # 菜的价格
    price = models.IntegerField()
    # 菜的描述
    desc = models.TextField(null=True, blank=True)
    # 菜的图片
    avatar = models.ImageField(null=True, blank=True) # 这里没有设置upload_to,Django 会将它存储在默认的文件上传目录中(settings.MEDIA_ROOT)
    # 菜的类别
    category = models.CharField(
        max_length=20,
        choices=(
            ('Meat', 'Meat'),
            ('Vegetable', 'Vegetable'),
            ('Dessert', 'Dessert'),
            ('Beverage', 'Beverage'),
        ), 
        default="Meat",
    )

    class Meta:
        # 自定义表名
        db_table = 'cuisine'
        # 表别名(Django Admin)
        verbose_name = '菜品表'

        
