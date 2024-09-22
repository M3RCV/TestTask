from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class SPost(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int = Field(..., description="ID создателя поста")
    text: str = Field(..., min_length=1, description="текст поста")
    created_at: datetime = Field(..., description="Время создание поста")
    updated_at: datetime = Field(..., description="Время обновления данных о посте")

class SPostADD(BaseModel):
    user_id: int = Field(..., description="ID пользователя")
    text: str = Field(..., description="Текст поста")

class SPostUPD(BaseModel):
    post_id: int = Field(..., description="ID поста")
    text: str = Field(..., description="Новый текст поста")