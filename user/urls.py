from django.urls import path
from user import views

urlpatterns = [
    path('<int:id>', views.userIndex.as_view())
]