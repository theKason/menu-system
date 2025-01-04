# Menu_system小程序API接口1.0

声明：该文档参考自 https://www.byhy.net/py/django/doc_api_v1_2/

<br><br>

## 概述

___

本接口用于Menu_system系统 前后端系统之间的数据交互。

本接口中，所有请求（除了登录请求之外），必须在body中携带登录成功后服务端返回的token。

除了GET请求，所有的请求消息的消息体（如有），都是json格式。

所有的响应消息的消息体，都是json格式。

<br><br>

## 登录系统

____

### 请求消息

____

```
POST /profile/login HTTP/1.1
COntent-Type: application/x-www-form-urlencoded
```

### 请求参数

___

http 请求消息body中参数以格式 x-www-form-urlencoded 存储
需要携带如下参数，

- code
  用户登录凭证（有效期五分钟）。开发者需要在开发者服务器后台调用 code2Session，使用 code 换取 openid、unionid、session_key 等信息

### 响应消息

___

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

___

http 响应消息 body 中， 数据以json格式存储，
如果登录成功，返回如下

```
{
    "token": xxxxx.
    "user_openid": xxxxx
}
```

如果登录失败，返回如下

```
{
    "error": "Login failed"
}
```
<br><br>


## 用户

___

### 列出用户

___

#### 请求消息

```
GET /profile?openid=xxxxx HTTP/1.1
```

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http响应消息body中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
    "name": xxxxx,
    "avatar": xxxxx
}
```

<br>

### 添加用户

____

#### 请求消息

```
POST /login HTTP/1.1
Content-Type: application/json
```

#### 请求参数

http 请求消息body携带添加客户的信息

消息体的格式是json，如下示例：

```
{
    "openid": xxxxx,
    "name": xxxxx,
    "avatar": xxxxx
}
```

其中

`openid` 表示小程序用户唯一标识

`name`和`avatar` 非必需字段

此URL同时适用于登录用户

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http响应消息body中，数据以json格式存储，

如果登录成功，返回如下

```
{
    "token": xxxxx.
    "user_openid": xxxxx
}
```

如果登录失败，返回如下

```
{
    "error": "Login failed"
}
```

<br>

### 修改用户信息

____

#### 请求消息

```
PUT /profile HTTP1.1
Content-Type: application/json
```

#### 请求参数

http请求消息body携带修改客户的信息

消息体的格式是json，如下示例：

```
{
    "openid": xxxxx,
    "name": xxxxx,
    "avatar": xxxxx
}
```

其中

除了`openid`，其余均为非必需字段。

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http响应消息body中，数据以json格式存储，

如果修改成功，返回如下

```
{
    "msg": "用户信息更改成功"
}
```

如果修改失败，返回如下

```
{
    "msg": "修改用户信息失败"
}
```

<br>

### 删除用户

____

#### 请求消息

```
DELETE /profile HTTP/1.1
Content-Type: application/json
```

#### 请求参数

http请求消息body携带要删除客户的openid

消息体的格式是json，如下示例：

```
{
    "openid": xxxxx
}
```

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http响应消息body中，数据以json格式存储，

如果删除成功，返回如下

```
{
    "msg": "用户删除成功"
}
```

如果删除失败，返回失败的原因，实例如下

```
{
    "msg": "删除用户失败"
}
```
<br><br>

## 菜品

____

### 列出菜品

____

#### 请求消息

```
GET /cuisine HTTP/1.1
```

#### 请求参数

此API无需携带任何请求参数

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http响应消息body中，数据以json格式存储，

如果获取信息成功，返回如下

```
[
    {
        "category_id": xxx,
        "name": xxx,
        "dishes": [
            {
                "cuisine_id": xxx, 
                "name": xxx, 
                "price": xxx, 
                "sales": xxx,
                "desc": xxx,
                "avatar": xxx
            }
        ]
    }
]
```

数据以 json 格式的列表返回，其中每个对象为菜品分类，

而每个菜品分类以中 key 为`dishes`的值是一个含有多个菜品对象的列表，

其中

`sales` 为该菜品销售数量，通菜品与订单的中间表 `OrderCuisine` 查询

`desc` 为对于该菜品的简短介绍

`avatar` 为菜品图片，如创建菜品时缺失，系统会自动添加默认文件

每个菜品信息已如下格式存储

```
{
  "cuisine_id": xxx, 
  "name": xxx, 
  "price": xxx, 
  "sales": xxx,
  "desc": xxx,
  "avatar": xxx
}
```

<br>

### 添加一个菜品

____

#### 请求消息

```
POST /cuisine HTTP/1.1
Content-Type: application/json
```

#### 请求参数

http请求消息body携带添加药品的信息

消息体的格式是json，如下示例：

```
{
    "name": xxx, 
    "price": xxx, 
    "desc": xxx,
    "avatar": xxx,
    "category": xxx
}
```

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```
{
    "id": xxxxx,
    "msg": "菜品创建成功"
}
```

如果添加失败，返回失败的原因，示例如下

```
{
    "msg": "所需字段缺少"
}
```

<br>

### 修改菜品信息

____

#### 请求消息

```
PUT  /cuisine HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带修改药品的信息

消息体的格式是json，如下示例：

```
{
    "id": xxxxx,
    "name": xxxxx,
    "price": xxxxx,
    "desc": xxxxx,
    "avatar": xxxxx,
    "category": xxxxx
}
```

其中

除 `id` 外，其余字段均非必需

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
    "msg": "菜品更改完成"
}
```

如果修改失败，返回失败的原因，示例如下

```
{
    "msg": "所需数据缺少"
}
```

<br>

### 删除菜品信息

____

#### 请求消息

```
DELETE  /cuisine HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除药品的id

消息体的格式是json，如下示例：

```
{
    "id": xxxxx
}
```

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
    "msg": "菜品删除成功"
}
```

如果修改失败，返回失败的原因，示例如下

```
{
    "msg": "菜品删除失败"
}
```

<br><br>

## 订单
___

### 列出订单
___

#### 请求消息
```
GET /order HTTP/1.1
```

#### 请求参数
http 请求消息 url 中 需要携带如下参数，

- user_openid
必填项，用户的唯一标识

#### 响应消息
```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容
http响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下
```
[
    {
        "id": xxxxx,
        "time_created": "2024-12-14T11:28:52.490Z",
        "cuisines": [
            {
                "name": xxxxx,
                "avatar": xxxxx
            }
        ]
    }
]
```
数据结构是包含多个订单字典对象的列表

其中

每个订单对象包括

`id` 订单ID

`time_created` 订单创建时间

`cuisines` 包含多个菜品字典对象的列表

<br>

### 创建订单
___

#### 请求消息
```
POST /cuisine HTTP/1.1
Content-Type: application/json
```
<br>

#### 请求参数
http 请求消息 body 携带添加药品的信息

消息体的格式是json，如下示例：
```
{
    "status": "已完成",
    "user_id": 1,
    "cuisines": 
    {
        "id1": amount1,
        "id2": amount2
    }
}
```
其中
`status` 订单状态
`user_openid` 用户唯一标识
`cuisines` 包含多个键值对（菜品ID & 该菜品数量）的字典
<br>

#### 响应消息
```
HTTP/1.1 200 OK
Content-Type: application/json
```
<br>

#### 响应内容
http 响应消息 body 中， 数据以json格式存储，

如果创建成功，返回如下
```
{
    'msg': '订单创建成功'
}
```
如果添加失败，返回失败的原因，示例如下
```
{
    'msg': '订单创建失败'
}
```
<br>

### 删除订单
___

#### 请求消息
```
DELETE /cuisine HTTP/1.1
Content-Type: application/json
```
<br>

#### 请求参数
http 请求消息 body 携带修改药品的信息

消息体的格式是json，如下示例：
```
{
    "order_id": xxxxx
}
```
<br>

#### 响应消息
```
HTTP/1.1 200 OK
Content-Type: application/json
```
<br>

#### 响应内容
http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下
```
{
    'msg': '订单删除成功'
}
```
如果添加失败，返回失败的原因，示例如下
```
{
    'msg': '订单删除失败'
}
```
