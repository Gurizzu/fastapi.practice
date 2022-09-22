from fastapi import status,HTTPException,Depends,Response,APIRouter
from src import models, schemas
from sqlalchemy.orm import Session
from src import database,oauth2


router = APIRouter(
    tags=['Votes']
)

@router.post('/votes',status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db : Session = Depends(database.get_db),
         current_user : int = Depends(oauth2.get_current_user)):
    
    
    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id)
    if post_query.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {vote.post_id} not found")
    
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    
    
    
    found_vote = vote_query.first()
    print(post_query.first())
    

    if( vote.dir == 1):
        
        
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f'user {current_user.id} has already voted on post {vote.post_id}')
            
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message" : "successfull added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        
        return {"message" : "successfull deleted post"}