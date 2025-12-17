import sqlite3
from pathlib import Path

db_path = Path("dev.db").resolve()
print("CWD:", Path().resolve())
print("DB :", db_path, "exists:", db_path.exists())

conn = sqlite3.connect(db_path)
tables = conn.execute("select name from sqlite_master where type='table'").fetchall()
print("Tables:", tables)
