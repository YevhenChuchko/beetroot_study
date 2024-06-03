import sqlite3
import hashlib

DB_USERS = "social_db.db"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(user_login, user_pwd, user_eye_color, user_mail, user_rating_qty):
    try:
        with sqlite3.connect(DB_USERS) as sqlite_conn:
            hashed_pwd = hash_password(user_pwd)
            sql_insert = """INSERT INTO social_users (user_login, user_pwd, user_eye_color, user_mail)
                            VALUES (?, ?, ?, ?);"""
            sqlite_conn.execute(sql_insert, (user_login, hashed_pwd, user_eye_color, user_mail))
            sqlite_conn.commit()
            print("User registered successfully")
    except sqlite3.IntegrityError:
        print(f"User with login {user_login} already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
