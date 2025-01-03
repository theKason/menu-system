from django.shortcuts import render
from django.views import View
from user.models import WeappUser
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
class userIndex(View):
    '''
    Django会根据请求方法自动调用类视图的对应函数

    请求数据结构:
    {
        "openid": string
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
            ID = reuqest.GET.get('openid')# 根据 URL 的 openid参数 去数据库查询
            obj = WeappUser.objects.get(openid=ID)
            return JsonResponse({"name": obj.name, "avatar": obj.avatar.url})
        except Exception as e:
            print(f'Error: {e}')
            return HttpResponse('该用户不存在')
        
    '''
    后续新建用户将由user.auth.wechat_login()一并处理
    '''
    # 处理 POST 请求（新建用户）
    # def post(self, request):
    #     '''
    #     请求数据结构(参数放在请求体, avatar可以缺失):
    #     {
    #         "user_name": "user2",
    #         "user_avatar": "/media/avatars/download2.jpeg"
    #     }
    #     '''
    #     try:
    #         user_data = json.loads(request.body)# 获取用户信息
    #         user_name = user_data.get('user_name')
    #         user_avatar = user_data.get('user_avatar')

    #         WeappUser.objects.create(
    #             name=user_name, 
    #             avatar=user_avatar)# 新增数据
    #     except Exception as e:
    #         print(f'Error: {e}')
    #         return HttpResponse('用户创建失败')
    #     else:
    #         return HttpResponse('用户创建成功')


    # 处理 PUT 请求（修改用户信息）
    def put(self, request):
        '''
        请求数据结构（参数放在请求体，name&avatar可以有可无）:
        {
            "openid": str,
            "name": str,
            "avatar: url(str)
        }
        '''

        try:
            user_data = json.loads(request.body)
            user_openid = user_data['openid']# 参数必须要有 id
            user_obj = WeappUser.objects.get(openid=user_openid)# 查看用户是否存在
            for param, value in user_data.items():
                if param == 'openid':# 无法修改用户openid
                    continue
                user_obj.__dict__[param] = value
                user_obj.save()
            return JsonResponse({'msg': '用户信息更改成功'})
        except Exception as e:
            print(f'Error: {e}')
            return JsonResponse({'msg': '修改用户信息失败'})

    # 处理 DELETE 请求（删除用户）
    def delete(self, request):
        '''
        请求数据结构（参数放在请求体）:
        {
            "openid": string
        }
        '''
        try:
            user_openid = json.loads(request.body).get('openid')
            WeappUser.objects.filter(openid=user_openid).delete()
            return JsonResponse({'msg':'用户删除成功'})
        except Exception as e:
            print(f'Error: {e}')
            return JsonResponse({'msg':'删除用户失败'})