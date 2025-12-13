# doebkblcya.com 个人网站

## 简介
本项目为 doebkblcya.com 个人导航与留言板网站，基于 FastAPI + SQLite + Nginx 架构，前端采用现代液态玻璃风格，适配多平台，支持留言功能。

## 架构说明
- **前端**：Jinja2 模板渲染，响应式设计，黑白灰液态玻璃风格，动画与高级字体。
- **后端**：FastAPI 框架，Python 3.12，留言数据存储于 SQLite。
- **数据库**：SQLite，单文件 guestbook.db，便于部署和备份。
- **Web服务器**：Nginx 反向代理，提供 HTTPS 访问，支持 WebSocket。

## 目录结构
```
/var/www/doebk_website/
├── app/
│   ├── __init__.py
│   ├── crud.py           # 数据库操作
│   ├── database.py       # 数据库连接配置
│   ├── models.py         # ORM模型
│   ├── routes/
│   │   ├── __init__.py
│   │   └── home.py       # 首页及留言板路由
│   ├── schemas.py        # Pydantic数据模型
│   ├── static/
│   │   └── style.css     # 前端样式
│   └── templates/
│       └── index.html    # 首页及留言板模板
├── guestbook.db          # SQLite数据库
├── main.py               # FastAPI应用入口
├── README.md             # 项目说明
└── venv/                 # Python虚拟环境
```

## 主要功能与修改
- 首页集成留言板，所有留言实时存储于 SQLite 并展示。
- 顶部导航栏采用毛玻璃风格，支持鼠标悬浮高亮。
- 全站字体升级，动画与响应式适配。
- Nginx 反向代理 FastAPI，支持 HTTPS。
- 目录结构清晰，便于后续扩展（如用户系统、更多子域名导航等）。

## 启动方式
1. 安装依赖：`pip install -r requirements.txt`
2. 启动 FastAPI：
   ```bash
   nohup uvicorn main:app --host 127.0.0.1 --port 8000 --workers 2 --proxy-headers > uvicorn.log 2>&1 &
   ```
3. 配置 Nginx 反向代理，重载 Nginx：
   ```bash
   sudo nginx -s reload
   ```
4. 访问 https://doebkblcya.com 查看效果。
---
如需二次开发或遇到问题，欢迎联系站长。

---
纯ai生成，ver.1