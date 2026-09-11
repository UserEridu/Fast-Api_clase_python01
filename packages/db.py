import sqlite3
from sqlite3 import Connection

DB_PATH: str = './data/rep.db'

def conexion_bd() -> Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn