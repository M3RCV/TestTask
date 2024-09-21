from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.exc import DatabaseError

from app.users.dao import UserDAO
from app.users.schemas import SUser, SUserADD, SUserUPD
from app.users.rd import RBUser

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
        user.hash_password()
        check = await UserDAO.add(**user.dict())
        if check:
            return {'message': "пользователь успешно создан", "ID": user}
        else:
            return {'message': "Ошибка при создании пользователя"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail="Неверный формат данных"+ str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail="Ошибка базы данных" + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Произошла внутренняя ошибка сервера"+ str(e))

@router.put("/update_description")
async def update_user_description(user: SUserUPD) -> dict:
    try:
        user.hash_password()
        check = await UserDAO.update(filter_by={'username': user.username}, password=user.password)
        if check:
            return {'message': "Данные о пользователе успешно обновлены", "ID": user}
        else:
            return {'message': "Ошибка при обновлении данных"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail="Неверный формат данных"+ str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail="Ошибка базы данных" + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Произошла внутренняя ошибка сервера"+ str(e))


