# board_app/models.py
from pydantic import BaseModel

class Board(BaseModel):
    id: int
    title: str
    content: Optional[str] = None

class BoardCreate(BaseModel):
    title: str
    content: Optional[str] = None

class BoardUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None