# board_app/routers/board.py
from typing import List, Optional
from fastapi import APIRouter, HTTPException, status
from models import Board, BoardCreate, BoardUpdate
import aiosqlite

router = APIRouter(prefix="/board", tags=["board"])

async def get_db():
    db = await aiosqlite.connect('board.db')
    await db.execute('''
        CREATE TABLE IF NOT EXISTS boards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT
        )
    ''')
    await db.commit()
    return db

@router.post("/", response_model=Board, status_code=status.HTTP_201_CREATED)
async def create_board(board: BoardCreate):
    async with await get_db() as db:
        await db.execute("INSERT INTO boards (title, content) VALUES (?, ?)", (board.title, board.content))
        await db.commit()
        await db.execute("SELECT * FROM boards WHERE id = last_insert_rowid()")
        row = await db.fetchone()
        return Board(id=row[0], title=row[1], content=row[2])

@router.get("/", response_model=List[Board])
async def read_boards():
    async with await get_db() as db:
        await db.execute("SELECT * FROM boards")
        rows = await db.fetchall()
        return [Board(id=row[0], title=row[1], content=row[2]) for row in rows]

@router.get("/{board_id}", response_model=Board)
async def read_board(board_id: int):
    async with await get_db() as db:
        await db.execute("SELECT * FROM boards WHERE id = ?", (board_id,))
        row = await db.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Board not found")
        return Board(id=row[0], title=row[1], content=row[2])

@router.put("/{board_id}", response_model=Board)
async def update_board(board_id: int, board: BoardUpdate):
    async with await get_db() as db:
        await db.execute("UPDATE boards SET title = ?, content = ? WHERE id = ?", (board.title, board.content, board_id))
        await db.commit()
        await db.execute("SELECT * FROM boards WHERE id = ?", (board_id,))
        row = await db.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Board not found")
        return Board(id=row[0], title=row[1], content=row[2])

@router.delete("/{board_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_board(board_id: int):
    async with await get_db() as db:
        await db.execute("DELETE FROM boards WHERE id = ?", (board_id,))
        await db.commit()
        await db.execute("SELECT * FROM boards WHERE id = ?", (board_id,))
        row = await db.fetchone()
        if row is not None:
            raise HTTPException(status_code=404, detail="Board not found")