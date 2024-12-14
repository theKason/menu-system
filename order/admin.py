from django.contrib import admin
from order.models import Order, OrderCuisine

def get_cuisine(obj):
    return OrderCuisine.objects.filter(order=obj.id)

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # 要展示的内容
        list_display = ['status','time_created',get_cuisine,'customer']

get_cuisine.short_description = 'Cuisine' # 设置列标题