from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import home

app = FastAPI()

# 挂载静态文件
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 注册首页路由
app.include_router(home.router)
