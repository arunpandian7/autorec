from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlmodel import Session
from backend.app.db.db import get_session, init_db
from backend.app.model import Orders


app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/add_data")
async def add_data(order: Orders, session: Session = Depends(get_session)):
    
    session.add(order)
    session.commit()
    await session.refresh(order)
    return order
