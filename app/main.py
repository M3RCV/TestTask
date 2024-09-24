from fastapi import FastAPI
from app.posts.routers import router as router_posts
from app.users.auth_router import router as router_auth
from app.users.router import router as router_users

app = FastAPI(
    title="TestTask",
    description="A simple social network",
    version="0.1.0"

)

@app.get("/")
def home_page():
    return {"message": "Главная страница"}

app.include_router(router_posts)
app.include_router(router_auth)
app.include_router(router_users)