from app.storage.db import engine

try:
    conn = engine.connect()
    print("DB Connected Successfully")
    conn.close()
except Exception as e:
    print("DB Connection Failed:", e)