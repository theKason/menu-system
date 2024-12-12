from django.contrib import admin
from order.models import Order, OrderCuisine

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # 要展示的内容
        list_display = ['order_status','time_created','get_cuisine','customer']

        def get_cuisine(self, obj):
                return OrderCuisine.objects.get(order=obj.id)
        get_cuisine.short_description = 'Cuisine' # 设置列标题

