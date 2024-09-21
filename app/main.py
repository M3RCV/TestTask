from fastapi import FastAPI
from app.users.router import router as router_students
from app.posts.routers import router as router_posts
from app.users.auth_router import router as router_auth

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}

app.include_router(router_students)
app.include_router(router_posts)
app.include_router(router_auth)