from django.db import models
from cuisine.models import Cuisine
from user.models import User

# Create your models here.
class Order(models.Model):
    # 订单状态: key会存入数据库，value可以通过get_order_status_display()获取
    order_status = {
        "1": "未完成",
        "2": "已完成",
        }
    
    # 订单创建时间
    time_created = models.DateTimeField(auto_now_add=True)

    # 订单商品: 一个订单可以包含多种商品
    # Order表和Cuisine表的多对多关系通过through参数指定的OrderCuisine表来确定
    cuisines = models.ManyToManyField(Cuisine, through="OrderCuisine")

    # 订单用户：一个用户关联多个订单
    # 数据库使用 外键 来表示一对多的关系：如果一个表中 的 某个字段是外键，
    # 那就意味着 这个外键字段的记录的取值，只能是它关联表的某个记录的主键的值。
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderCuisine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.PROTECT)

    # 订单中菜品的数量
    amount = models.PositiveIntegerField()


