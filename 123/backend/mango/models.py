from typing import Optional
from pydantic import BaseModel


class UserOut(BaseModel):
    email: str
    name: str
    lastname: str


class Comment(BaseModel):
    comment: str
    user_id: Optional[str]