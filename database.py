import sqlite3
from datetime import datetime

DB_NAME = "habits.db"

def init_db():
    """Veritabanını ve habits tablosunu oluşturur."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            habit_name TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_habit(user_id: int, habit_name: str):
    """Kullanıcı için bugünün tarihine alışkanlık ekler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    
    cursor.execute(
        "INSERT INTO habits (user_id, habit_name, date) VALUES (?, ?, ?)",
        (user_id, habit_name.lower(), today)
    )
    conn.commit()
    conn.close()

def get_habits_by_date(user_id: int, date_str: str = None):
    """Kullanıcının belirli bir gündeki (varsayılan bugün) alışkanlıklarını getirir."""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT habit_name FROM habits WHERE user_id = ? AND date = ?",
        (user_id, date_str)
    )
    habits = [row[0] for row in cursor.fetchall()]
    conn.close()
    return habits

def delete_habit(user_id: int, habit_name: str):
    """Kullanıcının bugünkü belirli bir alışkanlık kaydını siler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    
    cursor.execute(
        "DELETE FROM habits WHERE user_id = ? AND habit_name = ? AND date = ?",
        (user_id, habit_name.lower(), today)
    )
    # Etkilenen satır sayısını kontrol etmek için rowcount alıyoruz
    changes = conn.total_changes
    conn.commit()
    conn.close()
    return changes > 0
