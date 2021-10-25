from typing import Optional
from beanie import Document

class User(Document):
    email: str
    name: str
    lastname: str
    password: str

class CreatedBy(Document):
    created_by: Optional[str]
    name: str
    desc: str