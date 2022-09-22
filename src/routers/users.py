from typing import List
from fastapi import status,HTTPException,Depends,Response,APIRouter
from sqlalchemy.orm import Session
from src import models,schemas,utils
from src.database import get_db


router = APIRouter(
    tags=['Users']
)


@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponseUser)
def create_user(user : schemas.CreateUser,db : Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    me = models.User(**user.dict())
    db.add(me)
    db.commit()
    db.refresh(me)
    return me


@router.get("/users/get/{id}",response_model=schemas.ResponseUser)
def get_user(id : int,db : Session = Depends(get_db)):
    user = db.query(models.User).get(id)    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} was not found...")
    return user

@router.get("/users/get",response_model=List[schemas.ResponseUser])
def get_all_users(db : Session = Depends(get_db)):
    user = db.query(models.User).all()
    return user