"""
API视图 (View层) - MVT架构中的V
处理HTTP请求和响应
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

# 创建路由
router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=List[schemas.TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    """
    获取所有todos
    """
    todos = db.query(models.Todo).all()
    return todos


@router.post("/", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """
    创建新的todo
    """
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    根据ID获取单个todo
    """
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo_update: schemas.TodoUpdate, db: Session = Depends(get_db)):
    """
    更新todo
    """
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # 只更新非None的字段
    update_data = todo_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)
    
    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    删除todo
    """
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}