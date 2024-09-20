from app.core import BaseDAO
from app.models import Post

class PostDAO(BaseDAO):
    model = Post
