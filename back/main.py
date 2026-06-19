from fastapi import FastAPI
from database import engine
import models
from routes import notes,todos,total
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="我的一个便签工具", description="配合vue前端", version="1.0.0")
# 跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的源列表，空列表表示允许所有源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(notes.router, prefix="/notes", tags=["笔记"])
app.include_router(todos.router,prefix="/todos",tags=["任务"])
app.include_router(total.router,prefix="/total",tags=["统计"])


@app.get("/", tags=["根目录"])
async def read_root():
    return {"status": "success", "message": "后端正常", "data": None}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
