from fastapi import FastAPI

app = FastAPI(title="我的一个便签工具")

@app.get('/')
async def root():
    return{'status': 'success','message':'欢迎迎来到我的便签工具！','data': None} 