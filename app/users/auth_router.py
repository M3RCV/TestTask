from fastapi import APIRouter, HTTPException, status
from app.users.auth import get_password_hash
from app.users.dao import UserDAO
from app.users.schemas import SUserADD

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post("/register/")
async def register_user(user_data: SUserADD) -> dict:
    user = await UserDAO.find_by_username(this_username=user_data.username)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Пользователь с таким именем существует')
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UserDAO.add(**user_dict)
    return {'message':'вы успешно зарегестрированы'}
