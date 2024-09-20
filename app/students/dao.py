from app.core import BaseDAO
from app.models import User

class UserDAO(BaseDAO):
    model = User

