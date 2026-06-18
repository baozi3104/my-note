from fastapi import FastAPI
from database import engine
import models
from routes import notes,todos

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="我的一个便签工具", description="配合vue前端", version="1.0.0")

app.include_router(notes.router, prefix="/notes", tags=["笔记"])
app.include_router(todos.router,prefix="/todos",tags=["任务"])
app.include_router(total.router,prefix="/total",tags=["统计"])


@app.get("/", tags=["根目录"])
async def read_root():
    return {"status": "success", "message": "后端正常", "data": None}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
