from fastapi import FastAPI, Depends, HTTPException 
import services, models, schemas
from db import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "which book do you want"}


@app.get("/books/", response_model=list[schemas.Book])
def get_all_book(db: Session = Depends(get_db)):
    """获取所有书籍"""
    return services.get_books(db)


@app.get("/books/{id}", response_model=schemas.Book)
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    """获取指定 id 的书籍"""
    book_queryset = services.get_book(db, id)
    if book_queryset:
        return book_queryset
    else:
        raise HTTPException(status_code=404, detail="Invalid book id Provided")
        
    

@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """新增一本书籍"""
    return services.create_book(db, book) 

@app.put("/books/{id}", response_model=schemas.Book)
def update_book(id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    """更新指定书籍的信息"""
    # 传入新的书籍内容和对应的书籍 id 号
    update_target_book = services.update_book(db, book, id)
    if not update_target_book:
        raise HTTPException(status_code=404, detail="Book Not Found, update failed!")    
    return update_target_book

@app.delete("/books/{id}", response_model=schemas.Book)
def delete_book(id: int, db: Session = Depends(get_db)):
    """删除指定的书籍"""
    delete_target_book = services.delete_book(db, id)
    if delete_target_book:
        return delete_target_book
    else:
        raise HTTPException(status_code=404, detail="Book Not Found, can not delete!")