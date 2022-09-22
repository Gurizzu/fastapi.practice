from datetime import datetime
from pydantic import BaseModel,EmailStr
from typing import Optional,Union
from pydantic.types import conint

class Post(BaseModel):
    title:str
    content:str
    rating : Optional[int] = None
    
class PostUpdate(BaseModel):
    id:int
    title:str
    content:str
    
    class Config:
        orm_mode = True
        
        
        
class ResponseUser(BaseModel):
    id : int
    email : EmailStr
    created_at:datetime
    
    class Config:
        orm_mode = True
        
        
        
class ResponsePost(Post):
    id:int
    owner : ResponseUser
    
    class Config:
        orm_mode = True
        
class PostOut(BaseModel):
    Post: ResponsePost
    likes : int

    class Config:
        orm_mode = True
    
    
        

class CreateUser(BaseModel):
    email : EmailStr
    password : str
    
        
class UserLogin(BaseModel):
    email : EmailStr
    password : str
    
    
class Token(BaseModel):
    token_type : str
    access_token : str

class TokenData(BaseModel):
    id : Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    
        

