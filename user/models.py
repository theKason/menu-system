from django.db import models

# Create your models here.
class User(models.Model):
    # 用户名（感觉是调用微信api）
    name = models.CharField(max_length=30)

    # 用户头像（感觉是调用微信api）
    avatar = models.ImageField(upload_to='avatars/') # 该路径相对于MEDIA_ROOT(settings.py）

    class Meta:
        # 自定义表名
        db_table = 'user'
        # 表别名
        verbose_name = '用户表'