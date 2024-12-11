from django.urls import path
from . import views

urlpatterns = [
    path('<int: id>', views.userIndex.as_view())
]