from typing import Union

from fastapi import APIRouter,  HTTPException, status, Depends
from pydantic import ValidationError
from sqlalchemy.exc import DatabaseError

from app.models import User
from app.posts.dao import PostDAO
from app.posts.schemas import SPost, SPostUPD
from app.users.dependencies import get_current_user

router = APIRouter(prefix='/posts', tags=['Работа с постами'])

@router.get("/{user_id}/")
async def get_post_by_user_id(user_id: int) -> Union[list[SPost], dict]:
    try:
        result = await PostDAO.find_by_user_id(this_id=user_id)
        if result==[]:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Пользователь с ID {user_id} не опубликовал ни одного поста или такого пользователя не существует')
        return result
    except ValidationError as e:
        raise HTTPException(status_code=422, detail="Неверный формат данных " + str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail="Ошибка базы данных " + str(e))

@router.post("/add")
async def create_post(this_text: str, user_data: User = Depends(get_current_user)) -> dict:
    try:
        check = await PostDAO.add(**{'user_id': user_data.id, 'text': this_text})
        if check:
            return {'message': "Пост успешно опубликован"}
        else:
            return {'message': "Ошибка при добавлении поста"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail="Неверный формат данных " + str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail="Ошибка базы данных " + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Произошла внутренняя ошибка сервера " + str(e))

@router.delete("/delete/")
async def delete_post(post_id: int, user_data: User = Depends(get_current_user)) -> dict:
    try:
        check1 = await PostDAO.find_by_id(post_id)
        check2 = await PostDAO.check_user_id(user_data.id)
        if check1 is None or check2 is None:
            return {'message': "Поста не существует или он создан другим пользователем"}
        check = await PostDAO.delete(id=post_id)
        if check:
            return {"message": f"Пост с ID {post_id} удален!"}
        else:
            return {"message": "Ошибка при удалении поста!"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail="Неверный формат данных " + str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail="Ошибка базы данных " + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Произошла внутренняя ошибка сервера " + str(e))

@router.put("/update/")
async def update_post(post: SPostUPD, user_data: User = Depends(get_current_user)) -> dict:
    check1 = await PostDAO.find_by_id(post.post_id)
    check2 = await PostDAO.check_user_id(user_data.id)
    if check1 is None or check2 is None:
        return {'message': "Пост был удален или он создан другим пользователем"}
    check = await PostDAO.update(filter_by={'id': post.post_id}, text=post.text)
    if check:
        return {'message': "Пост успешно обновлен", 'anus': post}
    else:
        return {'message': "Ошибка при обновлении данных"}