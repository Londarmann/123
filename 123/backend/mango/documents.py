from typing import List, Optional 
from beanie import Document

from .models import Comment
class User(Document):
    email: str
    name: str
    lastname: str
    password: str

class Post(Document):
    created_by: Optional[str]
    name: str
    desc: str
    comments: Optional[List[Comment]] = []