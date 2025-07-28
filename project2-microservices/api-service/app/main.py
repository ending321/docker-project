from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def read_root():
    try:
        conn = mysql.connector.connect(
            host="192.168.31.17",  # MySQL主库地址
            user="root",
            password="chenjiewei",
            database="appdb"
        )
        return {"message": "Connected to database"}
    except Exception as e:
        return {"error": str(e)}
