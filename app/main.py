from fastapi import FastAPI, APIRouter
from .database import get_db, engine
from .routers import admin, auth, email

app = FastAPI(title="Patrasync(EmailSending)-API")

app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(email.router)


@app.get("/")
def root():
    return {"message": "Welcome To Patrasync(EmailSending)-API"}
