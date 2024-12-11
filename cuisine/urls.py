from django.urls import path
from . import views

urlpatterns = [
    # 使用类视图时，需要调用 as_view() 方法来将类视图转换为可调用的视图函数
    path("index/", views.cuisineIndex.as_view())
]