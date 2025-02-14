# Menu_system Mini Program API 1.0

Statement: This document is referenced from https://www.byhy.net/py/django/doc_api_v1_2/

<br><br>

## Overview

___

This API is used for data interaction between the front-end and back-end systems of the Menu_system.

In this API, all requests (except for login requests) must carry the token returned by the server after successful login in the body.

Except for GET requests, the message body of all requests (if any) is in JSON format.

The message body of all response messages is in JSON format.

<br><br>

## Login System

____

### Request Message

____

```
POST /profile/login HTTP/1.1
COntent-Type: application/x-www-form-urlencoded
```


### Request Parameters

___

The parameters in the http request message body are stored in x-www-form-urlencoded format.
The following parameters need to be carried:

- code
  User login credential (valid for five minutes). Developers need to call code2Session on the developer server backend to exchange the code for openid, unionid, session_key, etc.

### Response Message

___


```
HTTP/1.1 200 OK
Content-Type: application/json
```


### Response Content

___

In the http response message body, the data is stored in JSON format.
If the login is successful, the following is returned:

```
{
    "token": xxxxx.
    "user_openid": xxxxx
}
```


If the login fails, the following is returned:

```
{
    "error": "Login failed"
}
```
<br><br>


## User

___

### List Users

___

#### Request Message

```
GET /profile?openid=xxxxx HTTP/1.1
```

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the information is successfully obtained, the following is returned:

```
{
    "name": xxxxx,
    "avatar": xxxxx
}
```

<br>

### Add User

____

#### Request Message

```
POST /login HTTP/1.1
Content-Type: application/json
```

#### Request Parameters

The http request message body carries the information of the customer to be added.

The message body is in JSON format, as shown in the following example:

```
{
    "openid": xxxxx,
    "name": xxxxx,
    "avatar": xxxxx
}
```

Where

`openid` represents the unique identifier of the mini program user.

`name` and `avatar` are non-required fields.

This URL is also applicable for user login.

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the login is successful, the following is returned:

```
{
    "token": xxxxx.
    "user_openid": xxxxx
}
```

If the login fails, the following is returned:

```
{
    "error": "Login failed"
}
```

<br>

### Modify User Information

____

#### Request Message

```
PUT /profile HTTP1.1
Content-Type: application/json
```

#### Request Parameters

The http request message body carries the information of the customer to be modified.

The message body is in JSON format, as shown in the following example:

```
{
    "openid": xxxxx,
    "name": xxxxx,
    "avatar": xxxxx
}
```

Where

Except for `openid`, the rest are non-required fields.

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the modification is successful, the following is returned:

```
{
    "msg": "User information modified successfully"
}
```

If the modification fails, the following is returned:

```
{
    "msg": "Failed to modify user information"
}
```

<br>

### Delete User

____

#### Request Message

```
DELETE /profile HTTP/1.1
Content-Type: application/json
```

#### Request Parameters

The http request message body carries the openid of the customer to be deleted.

The message body is in JSON format, as shown in the following example:

```
{
    "openid": xxxxx
}
```

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the deletion is successful, the following is returned:

```
{
    "msg": "User deleted successfully"
}
```

If the deletion fails, the reason for the failure is returned, as shown in the following example:

```
{
    "msg": "Failed to delete user"
}
```
<br><br>

## Dishes

____

### List Dishes

____

#### Request Message

```
GET /cuisine HTTP/1.1
```

#### Request Parameters

This API does not require any request parameters.

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the information is successfully obtained, the following is returned:

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

The data is returned in a JSON format list, where each object is a dish category,

and the value of the key `dishes` in each dish category is a list containing multiple dish objects,

where

`sales` is the sales quantity of the dish, queried through the intermediate table `OrderCuisine` between dishes and orders.

`desc` is a brief introduction to the dish.

`avatar` is the dish image. If missing when creating the dish, the system will automatically add a default file.

Each dish information is stored in the following format:

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

### Add a Dish

____

#### Request Message

```
POST /cuisine HTTP/1.1
Content-Type: application/json
```

#### Request Parameters

The http request message body carries the information of the dish to be added.

The message body is in JSON format, as shown in the following example:

```
{
    "name": xxx, 
    "price": xxx, 
    "desc": xxx,
    "avatar": xxx,
    "category": xxx
}
```

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the addition is successful, the following is returned:

```
{
    "id": xxxxx,
    "msg": "Dish created successfully"
}
```

If the addition fails, the reason for the failure is returned, as shown in the following example:

```
{
    "msg": "Required fields are missing"
}
```

<br>

### Modify Dish Information

____

#### Request Message

```
PUT  /cuisine HTTP/1.1
Content-Type:   application/json
```

#### Request Parameters

The http request message body carries the information of the dish to be modified.

The message body is in JSON format, as shown in the following example:

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

Where

Except for `id`, the rest are non-required fields.

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the modification is successful, the following is returned:

```
{
    "msg": "Dish modified successfully"
}
```

If the modification fails, the reason for the failure is returned, as shown in the following example:

```
{
    "msg": "Required data is missing"
}
```

<br>

### Delete Dish Information

____

#### Request Message

```
DELETE  /cuisine HTTP/1.1
Content-Type:   application/json
```

#### Request Parameters

The http request message body carries the id of the dish to be deleted.

The message body is in JSON format, as shown in the following example:

```
{
    "id": xxxxx
}
```

#### Response Message

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content

In the http response message body, the data is stored in JSON format.

If the deletion is successful, the following is returned:

```
{
    "msg": "Dish deleted successfully""
}
```

If the deletion fails, the reason for the failure is returned, as shown in the following example:

```
{
    "msg": "Failed to delete dish"
}
```

<br><br>

## Order
___

### List Orders
___

#### Request Message
```
GET /order HTTP/1.1
```

#### 请求参数
#### Request Parameters
The http request message url needs to carry the following parameters:

- user_openid
Required, the unique identifier of the user.

#### Response Message
```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### Response Content
In the http response message body, the data is stored in JSON format.

If the information is successfully obtained, the following is returned:
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
The data structure is a list containing multiple order dictionary objects.

Where

Each order object includes:

`id` Order ID

`time_created` Order creation time

`cuisines` A list containing multiple dish dictionary objects.

<br>

### Create Order
___

#### Request Message
```
POST /cuisine HTTP/1.1
Content-Type: application/json
```
<br>

#### Request Parameters
The http request message body carries the information of the order to be added.

The message body is in JSON format, as shown in the following example:
```
{
    "status": "Completed",
    "user_id": 1,
    "cuisines": 
    {
        "id1": amount1,
        "id2": amount2
    }
}
```
Where
`status` Order status
`user_openid` User unique identifier
`cuisines` A dictionary containing multiple key-value pairs (dish ID & quantity of the dish)
<br>

#### Response Message
```
HTTP/1.1 200 OK
Content-Type: application/json
```
<br>

#### Response Content
In the http response message body, the data is stored in JSON format.

If the creation is successful, the following is returned:
```
{
    'msg': 'Order created successfully'
}
```
If the addition fails, the reason for the failure is returned, as shown in the following example:
```
{
    'msg': 'Failed to create order'
}
```
<br>

### Delete Order
___

#### Request Message
```
DELETE /cuisine HTTP/1.1
Content-Type: application/json
```
<br>

#### Request Parameters
The http request message body carries the information of the order to be deleted.

The message body is in JSON format, as shown in the following example:
```
{
    "order_id": xxxxx
}
```
<br>

#### Response Message
```
HTTP/1.1 200 OK
Content-Type: application/json
```
<br>

#### Response Content
In the http response message body, the data is stored in JSON format.

If the deletion is successful, the following is returned:
```
{
    'msg': 'Order deleted successfully'
}
```
If the deletion fails, the reason for the failure is returned, as shown in the following example:
```
{
    'msg': 'Failed to delete order'
}
```
