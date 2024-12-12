from django.urls import path
from order import views

urlpatterns = [
    # 该路经上的 user_id 只对GET请求有用
    path('<int:user_id>/', views.orderIndex.as_view())
]