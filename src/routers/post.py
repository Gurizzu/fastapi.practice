from typing import List, Optional
from fastapi import status,HTTPException,Depends,Response,APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from src import models, oauth2, schemas
from src.database import get_db

router = APIRouter(
    tags=['Posts']
)


@router.get("/sqlalchemy/get",response_model= List[schemas.PostOut])
def test_post(db : Session = Depends (get_db),current_user : int = Depends(oauth2.get_current_user)):
    post_method = db.query(models.Post).all()
    
    result = db.query(models.Post,func.count(models.Vote.post_id).label("likes")).join(models.Vote,models.Vote.post_id == models.Post.id).group_by(models.Post.id).all()
    
    if not post_method:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
    
    return result

@router.get("/sqlalchemy/get/query",response_model= List[schemas.PostOut])
def test_post(db : Session = Depends (get_db),current_user : int = Depends(oauth2.get_current_user),
              limit : int = 10, skip : int = 0, title: Optional[str] = ""):
    
    post_method = db.query(models.Post).filter(models.Post.title.contains(title)).limit(limit).offset(skip).all()
    
    result = db.query(models.Post,func.count(models.Vote.post_id).label("likes")).join(models.Vote,models.Vote.post_id == models.Post.id).group_by(models.Post.id).all()
    
    if not post_method:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
    
    return result

@router.get("/sqlalchemy/get/search/{title}")
def search_title(title:str,db : Session = Depends (get_db),current_user : int = Depends(oauth2.get_current_user)):
    #post_method = db.query(models.Post).all()
    
    posts = db.query(models.Post).filter(models.Post.title.contains(title)).all()
    return posts


@router.get("/sqlalchemy/get/{id}",response_model=schemas.ResponsePost)
def test_post_one(id : int,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    post_method = db.query(models.Post).filter(models.Post.id == id).first()
    
    if post_method == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    
    if post_method.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="forbidden")
    
    return post_method


@router.post("/sqlalchemy/post",response_model=schemas.ResponsePost)
def create_post(post : schemas.Post,db : Session = Depends (get_db),current_user : int = Depends(oauth2.get_current_user)):

    print(current_user.email,current_user.id)
    
    me = models.Post(owner_id=current_user.id,**post.dict())
    db.add(me)
    db.commit()
    db.refresh(me)
    return me


@router.put("/sqlalchemy/update/{id}",response_model=schemas.PostUpdate)
def update(id :int,updated_post : schemas.Post,db :Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    post_method = db.query(models.Post).filter(models.Post.id == id)
    post = post_method.first()
    
    if post_method.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="forbidden")
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    post_method.update(updated_post.dict())
    db.commit()
    
    return(post_method.first())

@router.delete("/sqlalchemy/delete/{id}")
def test_post_one(id : int,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    post_method = db.query(models.Post).filter(models.Post.id == id)

    if post_method.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    
    if post_method.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="forbidden")
    
    
    post_method.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)