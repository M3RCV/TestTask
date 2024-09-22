from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.models import User
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user
from app.users.schemas import SUserADD, SUserUPD

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

@router.post("/login/")
async def auth_user(user_data: SUserUPD, response: Response):
    check = await authenticate_user(username=user_data.username, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверное имя пользователя или пароль')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

@router.get("/me/")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data

@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}