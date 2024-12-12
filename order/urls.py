from django.urls import path
from order import views

urlpatterns = [
    path('<int:user_id>/', views.orderIndex.as_view())
]