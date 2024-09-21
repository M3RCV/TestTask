from sqlalchemy import select

from app.core import BaseDAO
from app.database import async_session_maker
from app.models import User

class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def find_by_username(cls,this_username: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(username=this_username)
            result = await session.execute(query)
            return result.scalar_one_or_none()