# from fastapi import FastAPI,status,HTTPException,Response,APIRouter
# from src import pw
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import json
# from src import schemas


# router = APIRouter(
#     tags=['Latihan']
# )
    
    
# try:
#     conn = psycopg2.connect(host= 'localhost',
#                             database= 'fasapi',
#                             user='postgres',
#                             password=pw.PASSWORD,
#                             cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection succesfull")
    
# except Exception as error:
#     print("Connecting to database failed")
#     print(f'error {error}')
    

# # post_ex = [{
# #     "title" : "best food in your opinion",
# #     "content" : "i think nasi padang is the best one",
# #     "id" : 1
# # },{
# #     "title" : "best drinks in your opinion",
# #     "content" : "maybe booba is good",
# #     "id" : 2
# # },
# # {
# #     "title" : "what is your country",
# #     "content" : "my country is indonesia, but other times i will visit other country",
# #     "id" : 3
# # }]

# # def findone(id):
# #     for i in post_ex:
# #         if i["id"] == id:
# #             return i
        
# # def find_by_id(id):
# #     for i,value in enumerate(post_ex):
# #         if value["id"] == id:
# #             return i


# @router.get("/get-post")
# def data():
#     cursor.execute(""" SELECT * FROM post """)
#     post = cursor.fetchall()
#     return {"data":post}

# @router.post("/post",status_code=status.HTTP_201_CREATED)
# def create_post(post : schemas.Post):
#     cursor.execute(""" INSERT INTO post (title,content) VALUES (%s ,%s) RETURNING * """,(post.title,post.content))
#     post_data = cursor.fetchone()
#     conn.commit()
#     return {"This is your data : " : post_data}


# @router.get("/get-post/{id}")
# def post(id:int):  
#     cursor.execute(""" SELECT * FROM post WHERE id = %s """,(str(id),))
#     post_data = cursor.fetchone()   
#     conn.commit()

#     if not post_data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with id: {id} was not found")
#     return{"data":post_data}

# # @router.get("/get-latest-post")
# # def latest():
# #     fn = post_ex[-1]
# #     return {"This is the latest data : " : fn}


# @router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete(id:int):
#     try:
#         cursor.execute(f""" DELETE FROM post WHERE id= {id} """)
#         conn.commit()
#     except:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with id: {id} was not found, can't be delete")
  

    

# @router.put("/update/{id}",status_code=status.HTTP_205_RESET_CONTENT)
# def update(id: int, post :schemas.Post):
#     try:
#         cursor.execute(f""" SELECT "title", "content", "rating" FROM post WHERE id = {id} """)
#         post_data = cursor.fetchone()
#         old = json.dumps(post_data)
#         old = json.loads(old)
        
#         post_this = post.dict()
        
#         #title = old["title"] if not post_this['title'] else post_this['title']
#         if not post_this['title']:
#             title = old['title']
#         else:
#             title = post_this["title"]
            
#         content = old["content"] if not post_this['content'] else post_this['content']
#         rating = old["rating"] if not post_this['rating'] else post_this['rating']
        
#         cursor.execute(""" UPDATE post SET "title"= %s,"content"= %s,"rating"= '{rating}' WHERE id={id} RETURNING * """)
#         post_data2 = cursor.fetchone()
#         return {"data" : post_data2}
        
#     except:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with id: {id} was not found, can't be update")
    