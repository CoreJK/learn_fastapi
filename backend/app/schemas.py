"""
数据模板 (Template层) - MVT架构中的T
使用Pydantic进行数据验证和序列化
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TodoCreate(BaseModel):
    """创建Todo的数据结构"""
    title: str
    description: Optional[str] = ""


class TodoUpdate(BaseModel):
    """更新Todo的数据结构"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(BaseModel):
    """返回Todo的数据结构"""
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True  # 允许从ORM模型创建