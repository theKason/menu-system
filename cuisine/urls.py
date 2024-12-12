from django.urls import path
from cuisine import views

urlpatterns = [
    # 使用类视图时，需要调用 as_view() 方法来将类视图转换为可调用的视图函数
    # Django会根据请求方法自动调用类视图的对应函数
    path("/", views.cuisineIndex.as_view())
]