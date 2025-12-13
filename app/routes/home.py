from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    messages = crud.get_messages(db)
    return templates.TemplateResponse("index.html", {"request": request, "messages": messages})

@router.post("/", response_class=HTMLResponse)
def post_message(request: Request, name: str = Form(...), message: str = Form(...), db: Session = Depends(get_db)):
    crud.create_message(db, name, message)
    return RedirectResponse(url="/", status_code=303)
