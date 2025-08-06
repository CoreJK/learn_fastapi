# FastAPI TodoList 2天紧急开发计划

## 🚨 时间紧急：MVP最小可行产品策略

### 总体策略
- **简化架构**doList 2天紧急开发计划

## 🚨 时间紧急：MVP最小可行产品策略

### 总体策略
- **简化架构**：只：只核心分层（API + Service + 内存存储）
- **快速迭代**：跳过复杂的ORM，使用简保留核心分层（API + Service + 内存存储）
- **快速迭代**：跳过复杂的ORM，使用简
- **核心功能**：只实现CRUD基本操作
- **延后优化**：数据库持--

## 📋 Day 1: 项目基础  后端核心功能 (8小时)

### ⏰ 上午 (4小时): 项目基础 1.5小时)
```bash
# 1. 更新依赖  API层

#### 🕘 09:00-10:30: 项目初始化 (1.5小时)
```bash
# 1. 更新依赖 构 (15分钟)
mkdir -p backend/{app/{api,services分钟)
pdm add sqlalchemy pytest-asyncio httpx

# 2. 创建最小目录结构 (15分钟)
mkdir -p backend/{app/{api,servicesnd/app/{__init__.py,main.py}
touch backend/appy,todo_service.py}
touch backend/app/models/{__init__.py,todo.py}
touch backen__init__.py,todos.py}
touch backend/app/services/{__init__.py,todo_service.py}
touch backend/app/models/{__init__.py,todo.py}
touch backen 3. 基础配置 (60分钟)
```

**第一个TDD循环**:
- 🔴 10:30-12:00: 数据模型 + Schema (1.5小写API健康检查测试
- 🟢 实现FastAPI应用启动
- 🔵 添加CORS配置

#### 🕙 10:30-12:00: 数据模型 + Schema (1.5小
# 简化版Todo模型（时)

**第二个TDD循环**:
- 🔴 编写Todo模型测试
- 🟢 实现简单的Todo数据类
- 🔵 添加Pydantic Schema

```python
# 简化版Todo模型（: datetime存存储）
@dataclass
class Todo:
    id: int
    title: str
    completed: bool = False
    created_at: datetime ⏰ 下午 (4小时): + API实现

#### 🕐 13:00-15:00: Service层 (2小时)

**第三到t Todo List  
- 🔴🟢第七个TDD循环** (每个操作30分钟):
- 🔴🟢🔵 Create Todo
- 🔴🟢🔵 Get Todo List  
- 🔴🟢odo
-ice（内存存储） Delete Todo

```python
# 简化版Service（内存存储）:
        self._todos:
    def __init__(self):
        self._todos: 1
    
    def create_todo(self, todo_data: TodoCreate) -> Todo:
        self._next_id = 1
    
    def create_todo(self, todo_data: TodoCreate) -> Todo:/todos简实现
```

#### 🕒 15:00-17:00: API路由实现 (2小时)

**第八到第十二个TDD循环**:
- 🔴🟢🔵 POST /todosETE /todos/{id}

###todos/{id}
- 🔴🟢🔵 PUT /todos/{id}
- 🔴🟢🔵 DELETE /todos/{id}

### 所有API的单元测试
- [ ]启动并响应请求

---

##动生成
- [ ] 服务器可以启动并响应请求

---

## 上午 (4小时): Vue3前端开发

#### 🕘 09:00- 📋 Day 2: 前端 + 集成 (8小时)

### ⏰ 上午 (4小时): Vue3前端开发

#### 🕘 09:00-tend
cd frontend
npm10:00: 前端项目初始化 (1小时)
```bash
# 创建Vue3项目
npm create vue@latest frontend
cd frontend
npm心组件开发 (2小时)

**最│   ├── TodoItem.vue     # 单个Todo项
│   ├── TodoList.vue小化组件结构**:do列表
│   └── TodoForm.vue     # 添加Todo表单
├── services/
│   └── api.js           # API调用
└── App.vue              # 主应用
```

**快速开发策略**:
- 使用Vue3组合式API
- 最简样式（基础CSS）
- 内联状态管理（不用Vuex/Pinia）

#### 🕚 11:00-12:00: API集成 (1小时)
```javascript
// services/api.js - 简化版API服务
const API_BASE = 'http://localhost:8000'

export const todoApi = {
    async getTodos() { /* ... */ },
    async createTodo(todo) { /* ... */ },
    // ... 其他CRUD操作
}
```

### ⏰ 下午 (4小时): 完善功能 + 部署

#### 🕐 13:00-15:00: 功能完善 (2小时)

**核心功能实现**:
- ✅ 显示Todo列表
- ✅ 添加新Todo
- ✅ 标记完成/未完成
- ✅ 删除Todo
- ✅ 简单的错误处理

#### 🕒 15:00-16:00: 样式美化 (1小时)
- 基础响应式布局
- 简单的动画效果
- 基本的UI反馈

#### 🕓 16:00-17:00: 集成测试 + 部署 (1小时)
- 前后端联调
- 基本的E2E测试
- 本地部署验证

### 🎯 Day 2 交付目标
- [ ] 完整的Vue3前端应用
- [ ] 前后端完全集成
- [ ] 基本的用户界面
- [ ] 可以正常使用的TodoList应用

---

## 🛠️ 技术栈简化版

### 后端
- **框架**: FastAPI
- **数据存储**: 内存字典 (简化版，无数据库)
- **测试**: Pytest + httpx
- **架构**: API + Service (两层架构)

### 前端  
- **框架**: Vue3 (组合式API)
- **HTTP客户端**: Axios
- **样式**: 原生CSS (无UI框架)
- **状态管理**: 组件内状态 (无Vuex)

---

## ⚡ 快速开发技巧

### TDD极简版
- **红**: 写最简单的失败测试 (5分钟)
- **绿**: 写最少代码让测试通过 (10分钟)  
- **重构**: 简单重构 (5分钟)
- **每个循环20分钟**

### 时间管理
- ⏰ 设置25分钟计时器 (番茄工作法)
- 🎯 每小时完成2-3个TDD循环
- 🚫 避免过度设计
- ✅ 优先完成核心功能

### 应急预案
如果时间不够，可以砍掉的功能：
1. 前端美化样式
2. 复杂的错误处理
3. 数据验证
4. 测试覆盖率优化

必须保留的核心功能：
1. 基本CRUD操作
2. 前后端通信
3. 基础用户界面

---

## 📦 最终交付清单

### 后端 ✅
- [ ] 5个API端点正常工作
- [ ] 基本的单元测试
- [ ] Swagger文档
- [ ] 服务可以启动

### 前端 ✅  
- [ ] 显示Todo列表
- [ ] 添加Todo
- [ ] 删除Todo
- [ ] 切换完成状态
- [ ] 基本样式

### 集成 ✅
- [ ] 前后端通信正常
- [ ] 错误处理基本可用
- [ ] 在浏览器中完整使用

---

## 🚀 开始执行

**现在开始第一个TDD循环！**

准备好了吗？让我们从最简单的API健康检查开始！

```bash
# 立即执行
pdm add sqlalchemy pytest-asyncio httpx
mkdir -p backend/{app/{api,services,models,schemas},tests}
```

你准备好开始了吗？ 🚀