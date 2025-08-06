"""
FastAPI应用入口
"""
from fastapi import FastAPI
from .database import engine
from . import models
from .views import router

# 创建数据库表
models.Base.metadata.create_all(bind=engine)

# 创建FastAPI应用
app = FastAPI(
    title="Todo List API",
    description="简单的Todo列表API，使用MVT架构",
    version="1.0.0"
)

# 注册路由
app.include_router(router)


@app.get("/")
def read_root():
    """
    根路径
    """
    return {
        "message": "Welcome to Todo List API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    """
    健康检查
    """
    return {"status": "healthy", "message": "Todo List API is running"}