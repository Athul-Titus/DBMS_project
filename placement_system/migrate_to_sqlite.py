import re

with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# Replace mysql.connector with sqlite3
app_code = app_code.replace('import mysql.connector', 'import sqlite3\nimport re')

# Modify get_db_connection()
new_db_connection = """def get_db_connection():
    try:
        connection = sqlite3.connect('placement.db')
        # We need a custom cursor or to replace %s with ? globally to make queries work.
        # SQLite doesn't understand %s.
        return connection
    except Exception as err:
        print(f"Database connection error: {err}")
        raise
"""

app_code = re.sub(
    r'def get_db_connection\(\):.*?return connection\n.*?except mysql\.connector\.Error as err:\n.*?print.*?raise\n',
    new_db_connection,
    app_code,
    flags=re.DOTALL
)

# For sqlite3, we shouldn't use db.commit() if it's not needed, but it's fine
# Replace cursor.execute(..., (...)) strings %s with ?
# A safer way to replace %s to ? in execute commands is to create a wrapper around cursor

wrapper_code = """
class SqliteCursorWrapper:
    def __init__(self, cursor):
        self.cursor = cursor
        
    def execute(self, query, params=None):
        query = query.replace('%s', '?')
        if params:
            return self.cursor.execute(query, params)
        return self.cursor.execute(query)
        
    def fetchone(self): return self.cursor.fetchone()
    def fetchall(self): return self.cursor.fetchall()
    def close(self): self.cursor.close()
    
def get_cursor(db):
    return SqliteCursorWrapper(db.cursor())
"""

# replace cursor = db.cursor() with cursor = get_cursor(db)
if 'class SqliteCursorWrapper' not in app_code:
    app_code = app_code.replace('def get_db_connection():', wrapper_code + '\ndef get_db_connection():')

app_code = app_code.replace('cursor = db.cursor()', 'cursor = get_cursor(db)')

# Remove mysql.connector exceptions
app_code = app_code.replace('except mysql.connector.Error as err:', 'except sqlite3.Error as err:')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Migration to sqlite script completed on app.py.")
