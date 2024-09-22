from sqlalchemy import select

from app.core import BaseDAO
from app.database import async_session_maker
from app.models import User
from sqlalchemy.exc import SQLAlchemyError
class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def find_by_username(cls,this_username: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(username=this_username)
            result = await session.execute(query)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result.scalar_one_or_none()

    @classmethod
    async def find_by_id(cls, this_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=this_id)
            result = await session.execute(query)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result.scalar_one_or_none()