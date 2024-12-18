from django.shortcuts import render
from django.views import View
from user.models import User
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
class userIndex(View):
    '''
    Django会根据请求方法自动调用类视图的对应函数

    请求数据结构:
    {
        "id": int
    }

    返回数据结构:
    {
        "name": "user1",
        "avatar": "/media/avatars/download.jpeg"
    }
    '''
    # 处理 GET 请求（获取用户信息）
    def get(self, reuqest):
        try:
            # 根据 URL 的 id参数 获取用户id去数据库查询
            ID = reuqest.GET.get('id')
            obj = User.objects.get(id=ID)
            return JsonResponse({"name": obj.name, "avatar": obj.avatar.url})
        except Exception as e:
            print(f'Error: {e}')
            return HttpResponse('该用户不存在')
        
    # 处理 POST 请求（新建用户）
    def post(self, request):
        '''
        请求数据结构(参数放在请求体, avatar可以缺失):
        {
            "user_name": "user2",
            "user_avatar": "/media/avatars/download2.jpeg"
        }
        '''
        try:
            # 获取用户信息
            user_data = json.loads(request.body)
            user_name = user_data.get('user_name')
            user_avatar = user_data.get('user_avatar')

            User.objects.create(
                name=user_name, 
                avatar=user_avatar)# 新增数据
        except Exception as e:
            print(f'Error: {e}')
            return HttpResponse('用户创建失败')
        else:
            return HttpResponse('用户创建成功')


    # 处理 PUT 请求（更改用户信息）
    def put(self, request):
        '''
        请求数据结构（参数放在请求体，name&avatar可以有可无）:
        {
            "id": int,
            "name": str,
            "avatar: url(str)
        }
        '''

        try:
            user_data = json.loads(request.body)
            # 参数必须要有 id
            user_id = user_data['id']
            # 查看用户是否存在
            user_obj = User.objects.get(id=user_id)
            # 忽略不存在的参数
            for param, value in user_data.items():
                if param == 'id':
                    continue
                user_obj.__dict__[param] = value
                user_obj.save()
            return HttpResponse('用户信息更改成功')
        except Exception as e:
            print(f'Error: {e}')
            return HttpResponse('该用户不存在')

    # 处理 DELETE 请求（删除用户）
    def delete(self, request):
        '''
        请求数据结构（参数放在请求体）:
        {
            "id": int
        }
        '''
        try:
            user_id = json.loads(request.body).get('id')
            User.objects.filter(id=user_id).delete()
            return HttpResponse('用户删除成功')
        except Exception as e:
            print(f'Error: {e}')
            return HttpResponse('用户删除不成功')