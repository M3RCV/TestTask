from fastapi import APIRouter, Depends, HTTPException
from app.students.dao import UserDAO
from app.students.schemas import SUser, SUserADD
from app.students.rd import RBUser

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей", response_model=list[SUser])
async def get_all_users(request_body: RBUser = Depends()) -> list[SUser]:
    return await UserDAO.find_all(**request_body.to_dict())

@router.get("/{id}", summary="получить пользователя по id")
async def get_user_by_id(user_id: int) -> SUser | dict:
    result = await UserDAO.find_by_id(user_id)
    if result is None:
        return {'message': f'пользователь с ID {user_id} не найден'}
    return result

@router.post("/create")
async def register_user(user: SUserADD) -> dict:
    try:
        check = await UserDAO.add(**user.dict())
        if check:
            return {'message': "пользователь успешно создан", "ID": user}
        else:
            return {'message': "Ошибка при создании пользователя"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Повторяющееся имя пользователя. Ошибка:" + str(e))