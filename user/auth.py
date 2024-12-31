import jwt
import datetime
import requests
from .models import WeappUser
from django.http import JsonResponse

# 定义密钥（生成token）

SECRET_KEY = 'weapp_created_by_wesley_and_kason'

def generate_token(user_id):
    '''
    生成JWT Token
    '''
    payload = {
        'user_id': user_id,
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
    app_id = "wxfd972ebc3f581169"
    app_secret = "your_app_secret"
    url = f"https://api.weixin.qq.com/sns/jscode2session?appid={app_id}&secret={app_secret}&js_code={code}&grant_type=authorization_code"
    response = requests.get(url)
    data = response.json()

    if 'openid' in data:
        openid = data['openid']
        session_key = data['session_key']

        # 查找或创建用户
        user, created = WeappUser.objects.get_or_create(openid=openid)

        # 生成 Token
        token = generate_token(user.id)

        # 返回 Token 给前端
        return JsonResponse({'token': token, 'user_id': user.id})

    return JsonResponse({'error': 'Login failed'}, status=400)


def authenticate_token(get_response):
    """
    中间件：验证 Token
    """
    def middleware(request):
        auth_header = request.headers.get('Authorization')
        # 请求不符合规范
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid Token'}, status=401)

        return get_response(request)
    return middleware

# 刷新 Token 接口（参考代码）
# def refresh_token(request):
#     """
#     刷新 Token
#     """
#     old_token = request.headers.get('Authorization').split(' ')[1]
#     try:
#         payload = jwt.decode(old_token, SECRET_KEY, algorithms=['HS256'], options={'verify_exp': False})
#         new_token = generate_token(payload['user_id'])
#         return JsonResponse({'token': new_token})
#     except jwt.InvalidTokenError:
#         return JsonResponse({'error': 'Invalid Token'}, status=401)