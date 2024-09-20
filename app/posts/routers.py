from fastapi import APIRouter,  HTTPException
from app.posts.dao import PostDAO
from app.posts.schemas import SPost, SPostADD

router = APIRouter(prefix='/posts', tags=['Работа с постами'])

@router.post("/add")
async def create_post(post: SPostADD) -> dict:
    try:
        check = await PostDAO.add(**post.dict())
        if check:
            return {'message': "Пост успешно опубликован", "ID": post.id}
        else:
            return {'message': "Ошибка при добавлении поста"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Отсутствующий id. Ошибка:" + str(e))

