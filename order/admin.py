from django.contrib import admin
from .models import Order, OrderCuisine, Cuisine

class OrderCuisineInline(admin.TabularInline):
    model = OrderCuisine
    extra = 1  # 默认显示一个空的关联行，可以增加/删除的数量

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'time_created', 'customer', 'get_cuisines')
    inlines = [OrderCuisineInline]  # 让订单与菜品的关系可以在订单的详情页进行编辑

    def get_cuisines(self, obj):
        # 返回与订单相关联的菜品名，用逗号分隔
        return ", ".join([cuisine.name for cuisine in obj.cuisines.all()])
    get_cuisines.short_description = '菜品'

admin.site.register(Order, OrderAdmin)

