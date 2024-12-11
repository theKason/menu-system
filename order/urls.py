from django.urls import path
from order import views

urlpatterns = [
    path('<int:id>/', views.orderIndex.as_view())
]