## mocker管理接口 ##

### 接口协议 ###

1. HTTP/1.1，端口8282

2. 前后端分离：/static 目录下提供静态文件服务，/api 目录提供api调用

### api接口原则 ###

1. Restful风格：

    接口使用restful风格，不同的HTTP方法对应不同的操作，而uri则对应被操作的实体，一般来说原则是：

    GET -- 读取

    POST -- 新增，语义为insert，创建新的对象，不保证幂等

    PUT -- 修改，语义为update，一般来说包含id，具有幂等性

    PATCH -- 部分修改，类似update，但是只替换对象中指定的字段，具有幂等性

    DELETE -- 删除

2. 统一出错返回：

    出错返回使用HTTP的4xx和5xx返回码，目前支持的出错是：

    400 -- 请求不合法

    500 -- 内部错误

    404 -- 没有对应的实体

    403 -- 认证/权限错误

    出错返回的内容是一个固定格式的JSON：
    ```
    {
        "errCode": 23, //内部定义的错误码
        "errMsg": "null pointer", //人类可读的错误信息
        "errDetail": ""  //详细的错误信息，可选。例如异常堆栈
    }
    ```

    下面的APIs说明中列出的返回均指正常返回，对应的HTTP返回代码是200/204。

3. 统一的分页信息：

    请求的分页信息用HTTP url参数传入，包括page和size两个参数，page表示第几页，页数从0开始；size表示每页有多少条数据。如果不传分页信息，则显示所有数据（page=0&size=MAX_INT）。

    返回的数据是一个列表，分页信息不在返回的数据中而是在HTTP返回头部中，HTTP头部中的分页信息在三个字段中：x-page，x-size，x-count：page表示第几页，页数从0开始；size表示每页有多少条数据；count表示数据的总数。

### API接口 ###

#### 项目管理 ####

管理需要mock的项目，每个服务包含一个名称，一段文字说明，关于项目行为的定义和项目的配置定义。

1. 读取服务列表：

    HTTP方法 GET，uri: /api/project

    可选参数：
    
    分页：page, size -- 整数，例如：page=0&size=20 表示首页数据，每页20条
            
    返回：
    ````
    Headers:
    x-page: 0
    x-size: 20
    x-count: 2
    
    [
      {
        "id": "12",
        "name": "test1",
        "desc": "test for xxxxxx",
        "behavior": 0,
        "config" : {
           "base_url": "https://club.jd.com/comment/productPageComments.action",
           "interval": 3600
        }
      },
      {
        "id": "13",
        "name": "test1",
        "desc": "test for xxxxxx"
        "behavior": 0,
        "config" : {
           "base_url": "https://club.jd.com/comment/productPageComments.action",
           "interval": 3600
        }
      }
    ]
    ````

    读取单个服务：
   
    HTTP方法 GET，uri: /api/project/{$_id}

    比如 GET /api/project/12
   
    返回：
    ````
    {
        "id": "12",
        "name": "test1",
        "desc": "test for xxxxxx",
        "behavior": 0,
        "config" : {
           "base_url": "https://club.jd.com/comment/productPageComments.action",
           "interval": 3600
        }
    }
    ````

2. 增加一个服务

    HTTP方法 POST，uri: /api/project
   
    提交：
    ````
    {
        "name": "test1",
        "desc": "test for xxxxxx",
        "behavior": 0,
        "config" : {
           "base_url": "https://club.jd.com/comment/productPageComments.action",
           "interval": 3600
        }
    }
    ````
   
    返回：
    ```
    {
        "id": "12",
        "name": "test1",
        "desc": "test for xxxxxx",
        "behavior": 0,
        "config" : {
           "base_url": "https://club.jd.com/comment/productPageComments.action",
           "interval": 3600
        }
    }
    ```

3. 删除一个服务

   HTTP方法 DELETE，uri: /api/project/{$_id}
   
   返回HTTP CODE 204，body无内容
