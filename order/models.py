from django.db import models
from cuisine.models import Cuisine
from user.models import WeappUser

# Create your models here.
class Order(models.Model):
    # 订单状态: 
    status = models.PositiveIntegerField()
    
    # 订单创建时间
    time_created = models.DateTimeField(auto_now_add=True)

    # 订单商品: 一个订单可以包含多种商品
    # Order表和Cuisine表的多对多关系通过through参数指定的OrderCuisine表来确定
    # 后续获取cuisines属性得到的也是 QuerySet对象
    cuisines = models.ManyToManyField(Cuisine, through="OrderCuisine")

    # 订单用户：一个用户关联多个订单
    # 数据库使用 外键 来表示一对多的关系：如果一个表中 的 某个字段是外键，
    # 那就意味着 这个外键字段的记录的取值，只能是它关联表的某个记录的主键的值。
    customer = models.ForeignKey(WeappUser, on_delete=models.CASCADE)

    class Meta:
        # 自定义表名
        db_table = 'order'
        # 表别名
        verbose_name = '订单表'

class OrderCuisine(models.Model):
    '''
    Order与Cuisine通过这张表实现 多对多 关系
    '''
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    # 订单中菜品的数量
    amount = models.PositiveIntegerField()

    class Meta:
        # 自定义表名
        db_table = 'ordercuisine'
        # 表别名
        verbose_name = '订单菜品关联表'


