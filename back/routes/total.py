from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal

# 你的逻辑 1：先在router文件夹里面建一个新的比如说total.py，建立新的路由
router = APIRouter()

# 你的逻辑 2：写一个通用的def get_db()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 你的逻辑 3：写一个查询函数比如说 def statistic
@router.get("/statistic")
def statistic(db: Session = Depends(get_db)):
    
    # 你的逻辑 4：查询数据库，赋值给一个变量
    # (.count() 就是让数据库去帮我们数一共有多少行)
    total_count = db.query(models.Note).count()
    
    # 你的逻辑 5：最后返回
    return {
        "message": "统计成功",
        "total_notes": total_count
    }