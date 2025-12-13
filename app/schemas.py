from pydantic import BaseModel
from datetime import datetime

class GuestbookMessageBase(BaseModel):
    name: str
    message: str

class GuestbookMessageCreate(GuestbookMessageBase):
    pass

class GuestbookMessageOut(GuestbookMessageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
