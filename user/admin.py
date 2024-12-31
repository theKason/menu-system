from django.contrib import admin
from user.models import WeappUser

# Register your models here.
@admin.register(WeappUser)
class OrderAdmin(admin.ModelAdmin):
    # 要展示的内容
        list_display = ['name','avatar']