from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class SUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="ID пользователя")
    username: str = Field(..., min_length=1, max_length=50, description="Имя пользователя от 1 до 50 символов")
    password: str = Field(..., min_length=1, max_length=50, description="пароль пользователя от 1 до 50 символов")
    created_at: datetime = Field(..., description="Время создания пользователя")
    updated_at: datetime = Field(..., description="Время обновления данных о пользователе")

class SUserADD(BaseModel):
    username: str = Field(..., description="имя пользователя")
    password: str = Field(..., description="пароль пользователя")

class SUserUPD(BaseModel):
    username: str = Field(..., description="Имя пользователя")
    password: str = Field(..., description="Пароль пользователя")
