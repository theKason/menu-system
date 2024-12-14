"""
URL configuration for menu_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cuisine import views as cuisine_views
from order import views as order_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # order, profile使用了 二级路由: 后续路径由应用各自管理
    path('cuisine/', cuisine_views.cuisineIndex.as_view()),# 使用类视图时，需要调用 as_view() 方法来将类视图转换为可调用的视图函数
    path('order/', order_views.orderIndex.as_view()),
    path('profile/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 想在浏览器通过指定路径访问到图片资源，还需要给图片资源配置一个路由入口。
