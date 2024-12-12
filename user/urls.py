from django.urls import path
from user import views

urlpatterns = [
    path('<int:user_id>', views.userIndex.as_view())
]