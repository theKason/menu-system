from django.contrib import admin
from user.models import User

# Register your models here.
@admin.register(User)
class OrderAdmin(admin.ModelAdmin):
    # 要展示的内容
        list_display = ['name','avatar']