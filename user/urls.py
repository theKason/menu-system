from django.urls import path
from . import auth, views

urlpatterns = [
    path('', views.userIndex.as_view()),
    path('login/', auth.wechat_login)
]
