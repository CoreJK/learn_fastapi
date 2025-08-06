"""
数据模型 (Model层) - MVT架构中的M
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base


class Todo(Base):
    """
    Todo数据模型
    """
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, default="")
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"<Todo(id={self.id}, title='{self.title}', completed={self.completed})>"