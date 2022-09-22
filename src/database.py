from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings_env
# import psycopg2
# from psycopg2.extras import RealDictCursor

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings_env.database_username}:{settings_env.database_password}@{settings_env.database_hostname}:{settings_env.database_port}/{settings_env.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
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