from pydantic import BaseModel

class TodoBase(BaseModel):
    completed: bool

class TodoCreate(BaseModel):
    content: str

class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    todos: list[Todo] = []

    class Config:
        orm_mode = True