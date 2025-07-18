from fastapi import FastAPI
from app.routers import board, column, task

app = FastAPI()

app.include_router(board.router)
app.include_router(column.router)
app.include_router(task.router)
