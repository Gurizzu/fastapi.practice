
from .database import Base
from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"
    
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    rating = Column(Integer,nullable=True, server_default='0')
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('NOW()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    
    owner = relationship("User")
    

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('NOW()'))
    
    
class Vote(Base):
    __tablename__ = "votes"
    
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True)