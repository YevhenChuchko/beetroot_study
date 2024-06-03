#                 PLAN  to take over the world of users :
#
# 1. Створити БД для користувачів social з полями:
#         а. user_id (має створюватися автоматично при реєстрації користувача)
#         b. user_login (as PRIMIARY KEY)
#         c. user_pswd
#         e. user_eye_color (для Нікіти)
#         f. user_@mail (хз навцщо, але нехай буде)
#         g. user_rating (може колись знадобиться)
#
# 2. Створити модуль реєстрації користувачів
#         а. Створити функцію хешування user_pswd
#
# 3. Переробити меню, враховуючи необхідність користувача логінитися
# 4. Переписати posts і comments в базу даних
# 5. Модифікувати модуль posts відповідно до змін вище
# 6. 7 разів подумать, чи треба мені таке щастя?
# _______________________________________________

import sqlite3

DB_USERS = "social_db.db"

def create_tables():
    try:
        with sqlite3.connect(DB_USERS) as sqlite_conn:
            print("Opened database successfully")
            sql_users = """CREATE TABLE IF NOT EXISTS social_users (
                user_login TEXT PRIMARY KEY,
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_pwd TEXT NOT NULL,
                user_eye_color TEXT NOT NULL,
                user_mail TEXT,
                user_rating_qty INTEGER
            );"""
            sql_posts = """CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                text TEXT NOT NULL,
                created_at TEXT NOT NULL,
                likes INTEGER DEFAULT 0,
                dislikes INTEGER DEFAULT 0,
                FOREIGN KEY (author) REFERENCES social_users(user_login)
            );"""
            sql_comments = """CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                post_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (author) REFERENCES social_users(user_login),
                FOREIGN KEY (post_id) REFERENCES posts(id)
            );"""
            sqlite_conn.execute(sql_users)
            sqlite_conn.execute(sql_posts)
            sqlite_conn.execute(sql_comments)
            print("Tables created successfully")
    except sqlite3.Error as e:
        print(f"ConnectionError: {e}")

if __name__ == "__main__":
    create_tables()
