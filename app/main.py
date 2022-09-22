from fastapi import FastAPI
from src import models
from src.database import engine
from fastapi.middleware.cors import CORSMiddleware
from src.routers import latihan, post,users,auth,votes

app = FastAPI()

origins = ['https://www.google.com/']

# models.Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(users.router)
# app.include_router(latihan.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
async def main():
    return {"message": "Hello World"}