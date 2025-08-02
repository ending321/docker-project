# api-service/app/main.py
from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# 测试数据库连接
@app.on_event("startup")
def test_db_connection():
    try:
        conn = mysql.connector.connect(
            host="mysql",  # 使用服务名而非IP
            port=3306,
            user="root",
            password="chenjiewei",
            database="appdb"
        )
        if conn.is_connected():
            print("数据库连接成功")
            conn.close()
    except Error as e:
        print(f"数据库连接失败: {e}")
        raise  # 失败时终止服务启动

# 定义根路径（处理 / 请求）
@app.get("/")
def root():
    return {"message": "API Service is running!"}

# 定义/api/路径（处理 /api/ 请求）
@app.get("/api/")
def api_root():
    return {"message": "This is the API root"}

# 定义具体API接口（如 /api/items）
@app.get("/api/items")
def get_items():
    return {"items": ["item1", "item2"]}

