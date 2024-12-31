from django.db import models

# Create your models here.
class Category(models.Model):
    # 分类名称
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        # # 自定义表名
        db_table = 'category'
        # 表别名(Django Admin)
        verbose_name = '分类表'


class Cuisine(models.Model):
    # 菜的名称
    name = models.CharField(max_length=20, unique=True) # CharField 必须要有max_length属性
    # 菜的价格
    price = models.IntegerField()
    # 菜的描述
    desc = models.TextField(null=True, blank=True)
    # 菜的图片
    avatar = models.ImageField(null=True, blank=True, default="default-avatar.jpeg") # 这里没有设置upload_to,Django会将它存储在默认的文件上传目录中(settings.MEDIA_ROOT)
    # 菜的类别
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        # 自定义表名
        db_table = 'cuisine'
        # 表别名(Django Admin)
        verbose_name = '菜品表'



        
