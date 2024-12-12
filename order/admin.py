from django.contrib import admin
from order.models import Order

# Register your models here.
@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    # 要展示的内容
        list_display = ['order_status','time_created','cuisine','customer']