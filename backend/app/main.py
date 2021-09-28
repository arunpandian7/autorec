from fastapi import FastAPI
from backend.app.db.db import init_db
from backend.app.api import v1
import uvicorn

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(v1.router, tags=["db_wrapper"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
