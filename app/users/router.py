from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.exc import DatabaseError

from app.users.auth import get_password_hash
from app.users.dao import UserDAO
from app.users.schemas import SUser, SUserADD, SUserUPD
from app.users.rd import RBUser

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.put("/update_description")
async def update_user_description(user: SUserUPD) -> dict:
    try:
        check = await UserDAO.update(filter_by={'username': user.username}, password=get_password_hash(user.password))
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


