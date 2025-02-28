# board_app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import board

app = FastAPI()

app.include_router(board.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)