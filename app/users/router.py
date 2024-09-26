from fastapi import APIRouter, Depends, HTTPException


from app.models import User
from app.users.dependencies import get_current_user


router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/me/") #функция которая выводит данные о пользователе
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data