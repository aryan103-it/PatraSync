from fastapi import FastAPI
from .database import get_db, engine

app = FastAPI(title="Patrasync(EmailSending)-API")


@app.get("/")
def root():
    return {"message": "Welcome To Patrasync(EmailSending)-API"}
