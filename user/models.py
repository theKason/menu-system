from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class WeappUser(AbstractUser):
    openid = models.CharField(max_length=255, unique=True, null=True, blank=True)
    unionid = models.CharField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=30)
    # 用户头像（感觉是调用微信api）
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) # 该路径相对于MEDIA_ROOT(settings.py）

    class Meta:
        # 自定义表名
        db_table = 'user'
        # 表别名(Django Admin)
        verbose_name = '用户表'