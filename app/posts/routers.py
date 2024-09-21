from fastapi import APIRouter,  HTTPException
from pydantic import ValidationError
from sqlalchemy.exc import DatabaseError

from app.posts.dao import PostDAO
from app.posts.schemas import SPost, SPostADD

router = APIRouter(prefix='/posts', tags=['Работа с постами'])

@router.post("/add")
async def create_post(post: SPostADD) -> dict:
    try:
        check = await PostDAO.add(**post.dict())
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

@router.delete("/delete/{post_id}")
async def delete_post(post_id: int) -> dict:
    try:
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