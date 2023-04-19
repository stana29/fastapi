from fastapi import APIRouter
import psycopg2
from pydantic import BaseModel

with open("password.txt", mode="r") as f:
    password = f.readline()
router = APIRouter(prefix="/sql")

connection = psycopg2.connect(
    host="localhost", user="postgres", password=password, database="mydb"
)


class UserInfo(BaseModel):
    name: str
    email: str
    password: str


@router.get("/test/")
def test():
    return {"a": "b"}


@router.delete("/all/")
def delete_all():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE users")
    return {"message": "all users deleted"}


@router.delete("/{id}/")
def delete_user(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE from users WHERE id = {id}")
            # connection.commit()
    return {"message": f"user {id} deleted"}


@router.post("/add/")
def add_user(user: UserInfo):
    with connection:
        with connection.cursor() as cursor:
            # レコードを挿入
            sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user.name, user.email, user.password))
            # コミットしてトランザクション実行
            connection.commit()
    return


@router.get("/all/")
def get_all_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            response = cursor.fetchall()
    return response


@router.get("/{id}")
def get_user(id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE id = {id}")
            response = cursor.fetchone()
    return response
