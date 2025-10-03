#

## 基础设置

- 项目环境配置
```shell
# 创建虚拟环境
python3 -m venv venv

# 设置pip镜象
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

```

## 服务启动&维护
- 项目依赖打包
```shell
#建议使用pipreqs
pipreqs  --force  --ignore venv ./

# 生成requirements.txt  (不建议，会将所有的扩展列出)，建议使用pipreqs
pip  freeze > requirements.txt

```

- 数据库迁移
```shell
# 当 fask 的应用入口在项目根目录，且文件名为app.py，并且实例变量名为 app 时
flask --app app.http.app db init # 初始化数据库
flask --app app.http.app db migrate # 迁移数据库
flask --app app.http.app db upgrade # 升级数据库
flask --app app.http.app db downgrade # 回滚数据库
flask --app app.http.app db drop # 删除数据库
```

- 服务维护
```shell
# flask 启动
flask --app app.http.app run
# flask 启动并监听端口
#flask --app app.http.app run --host=0.0.0.0 --port=5000

# 查看路由
flask --app app.http.app routes

```


## 服务架构
- LLMOPS 服务架构
![llmops-arch.png](resources%2Fllmops-arch.png)

- 项目目录结构

- 核心依赖 
```shell
# injector 依赖注入框架
pip install injector

# flask API   框架
pip install flask

# flask-wtf 表单校验框架，是基于wtforms封装的Flask插件，支持CSRF保护快速提取数据、自定义验证规则及wtforms的所有规则。
pip install flask-wtf

# 测试框架 py_test
pip install pytest

# 数据库驱动
pip  install flask-sqlalchemy psycopg2

# 项目依赖 pipreqs 生成requirements.txt
pip install pipreqs

# 数据库迁移
pip install flask-migrate

```

## API接口返回数据格式设计
- 响应状态码
```json
    success // 成功
    fail // 失败
    not_found // 资源不存在
    unauthorized // 未授权
    forbidden // 无权限
    validation_error // 参数验证错误
```
- 统一响应格式
```json
{
  "code": "success", // 状态码
  "message": "操作成功", // 状态码描述
  "data": {} // 数据
}
```
- 接口分页数据格式
```json
{
  "code": "success", // 状态码
  "message": "操作成功", // 状态码描述
  "data": {
    "pagenator": {
      "page_size": "10", // 每页大小
      "total_page" 10, //总页数
      "current_page": "1", // 当前页码
      "total_record": "100", // 总记录数
    },
    "list": [] // 数据列表
  } 
}
```

