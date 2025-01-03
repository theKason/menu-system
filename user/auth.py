import jwt
import datetime
import requests
from .models import WeappUser
from django.http import JsonResponse

# 定义密钥（生成token）
SECRET_KEY = 'weapp_created_by_wesley_and_kason'

def generate_token(user_openid, user_session_key):
    '''
    生成JWT Token
    '''
    # 自定义登陆态
    payload = {
        'user_openid': user_openid,
        'user_session_key': user_session_key,
        'exp': datetime.datetime.now() + datetime.timedelta(days=7),  # 7天过期
        'iat': datetime.datetime.now()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')# jwt库生成Token
    return token


def wechat_login(request):
    '''
    用户登陆并返回Token
    '''
    code = request.POST.get('code')

    # 通过微信接口获取 openid 和 session_key
    app_id = "xxxxx"
    app_secret = "xxxxx"
    url = f"https://api.weixin.qq.com/sns/jscode2session?appid={app_id}&secret={app_secret}&js_code={code}&grant_type=authorization_code"
    response = requests.get(url)
    data = response.json()

    if 'openid' in data:
        openid = data['openid']
        name = data['name']
        avatar = data['avatar']

        # 查找或创建用户
        # Returns a tuple of (object, created), where object is the retrieved or created object and created is a boolean specifying whether a new object was created.
        user, created = WeappUser.objects.get_or_create(
            openid=openid,
            name=name,
            avatar=avatar)

        # 生成 Token
        token = generate_token(user.openid)

        # 返回 Token 给前端
        return JsonResponse({'token': token, 'user_openid': user.openid})

    return JsonResponse({'error': 'Login failed'}, status=400)


def authenticate_token(get_response):
    """
    中间件：验证 Token
    """
    def middleware(request):
        # 检查 URL，如果是指定的路径则跳过中间件逻辑
        excluded_paths = ['/profile/login/', '/cuisine/']  # 不需要执行的路径
        if request.path in excluded_paths:
            return get_response(request)

        # 正常验证逻辑
        auth_header = request.headers.get('Authorization')
        # 请求不符合规范
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user_openid = payload['user_openid']
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid Token'}, status=401)

        return get_response(request)
    return middleware


# 刷新 Token 接口（参考代码）
def refresh_token(request):
    """
    刷新 Token
    """
    old_token = request.headers.get('Authorization').split(' ')[1]
    try:
        payload = jwt.decode(old_token, SECRET_KEY, algorithms=['HS256'], options={'verify_exp': False})
        new_token = generate_token(payload['user_openid'])
        return JsonResponse({'token': new_token})
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Invalid Token'}, status=401)