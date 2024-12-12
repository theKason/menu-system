from django.shortcuts import render
from django.views import View
from user.models import User
from django.http import JsonResponse, HttpResponse

# Create your views here.
class userIndex(View):
    '''
    Django会根据请求方法自动调用类视图的对应函数
    '''

    # 处理 GET 请求（获取用户信息）
    def get(self, reuqest):
        ID = reuqest.GET['id']
        try:
            # 根据 URL 的 id参数 获取用户id去数据库查询
            obj = User.objects.get(id=ID)
            return JsonResponse(obj)
        except:
            return HttpResponse('user does not exists')
        
    # 处理 POST 请求（新建用户）
    def post(self, request):
        # 获取用户信息
        user_name = request.POST.get('user_name')
        user_avatar = request.POST.get('user_avatar')

        new_user = User.objects.create(
            name=user_name, 
            avatar=user_avatar)# 新增数据
        
        new_user.save()# 保存


    # 处理 PUT 请求（更改用户）
    def put(self, request):
        user_id = request.PUT.get('user_id')
        user_name = request.PUT.get('user_name')
        user_avatar = request.PUT.get('user_avatar')

        # 查看用户是否存在
        try:
            User.objects.filter(id=user_id).update(
                name=user_name, avatar=user_avatar)
            return HttpResponse('用户信息更改成功')
        except:
            return HttpResponse('该用户不存在')

    # 处理 DELETE 请求（删除用户）
    def delete(self, request):
        user_id = request.DELETE.get('user_id')
        try:
            User.objects.filter(id=user_id).delete()
            return HttpResponse('用户删除成功')
        except:
            return HttpResponse('用户删除不成功')