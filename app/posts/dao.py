from app.core import BaseDAO
from app.models import Post
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
class PostDAO(BaseDAO):
    model = Post

    @classmethod
    async def find_by_user_id(cls, this_id: int): #метод поиска постов по ID пользователя
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(user_id=this_id)
            result = await session.execute(query)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result.scalars().all()

    @classmethod #метод для проверки того кому принадлежит пост
    async def check_user_id(cls, this_user_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(user_id=this_user_id)
            result = await session.execute(query)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result.scalars().all()
