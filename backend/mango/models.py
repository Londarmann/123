from pydantic import BaseModel


class UserOut(BaseModel):
    email: str
    name: str
    lastname: str


class CreatedBy(BaseModel):
    name: str
    desc: str