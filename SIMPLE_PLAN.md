# 简化版 FastAPI TodoList 开发计划

## 🎯 需求简化
- **架构模式**: MVT (Model-View-Template)
- **数据库**: SQLite3
- **功能**: 基础CRUD (增删查改)
- **开发方式**: 直接实现，不用TDD

## 📁 项目结构 (MVT模式)
```
learn_fastapi/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # 应用入口
│   │   ├── database.py          # 数据库配置
│   │   ├── models.py            # 数据模型 (M)
│   │   ├── schemas.py           # 数据模板 (T)
│   │   └── views.py             # API视图 (V)
│   └── todos.db                 # SQLite数据库文件
└── README.md
```

## 🛠️ 技术栈
- **FastAPI**: Web框架
- **SQLAlchemy**: ORM
- **SQLite3**: 数据库
- **Pydantic**: 数据验证和序列化
- **Uvicorn**: ASGI服务器

## 📋 实现步骤

### Step 1: 数据库配置 (database.py)
- SQLite连接配置
- 数据库会话管理

### Step 2: 数据模型 (models.py) - Model层
- Todo数据表定义
- 字段: id, title, description, completed, created_at

### Step 3: 数据模板 (schemas.py) - Template层  
- TodoCreate: 创建Todo的数据结构
- TodoUpdate: 更新Todo的数据结构
- TodoResponse: 返回Todo的数据结构

### Step 4: API视图 (views.py) - View层
- GET /todos - 获取所有todos
- POST /todos - 创建新todo
- GET /todos/{id} - 获取单个todo
- PUT /todos/{id} - 更新todo
- DELETE /todos/{id} - 删除todo

### Step 5: 应用入口 (main.py)
- FastAPI应用创建
- 路由注册
- 数据库初始化

## 🚀 CRUD接口设计

| 方法 | 路径 | 功能 | 请求体 | 响应 |
|------|------|------|--------|------|
| GET | `/todos` | 获取所有todos | - | `List[TodoResponse]` |
| POST | `/todos` | 创建todo | `TodoCreate` | `TodoResponse` |
| GET | `/todos/{id}` | 获取单个todo | - | `TodoResponse` |
| PUT | `/todos/{id}` | 更新todo | `TodoUpdate` | `TodoResponse` |
| DELETE | `/todos/{id}` | 删除todo | - | `{"message": "deleted"}` |

## 📦 数据结构

### TodoCreate
```json
{
  "title": "string",
  "description": "string"
}
```

### TodoUpdate  
```json
{
  "title": "string",
  "description": "string", 
  "completed": "boolean"
}
```

### TodoResponse
```json
{
  "id": 1,
  "title": "string",
  "description": "string",
  "completed": false,
  "created_at": "2024-01-01T00:00:00"
}
```

## ⚡ 快速开始
1. 创建数据库配置
2. 定义数据模型
3. 创建数据模板
4. 实现API视图
5. 启动应用测试

预计完成时间: 2-3小时