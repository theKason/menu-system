from django.contrib import admin
from cuisine.models import Cuisine

# Register your models here.
@admin.register(Cuisine)
class Cuisine(admin.ModelAdmin):
    # 要展示的内容
    list_display = ['name','desc','avatar','category']