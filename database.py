import sqlite3

# grab the queries
CREATE_CLOTHING_TABLE = "CREATE TABLE IF NOT EXISTS clothing(id INTEGER PRIMARY KEY, name TEXT, body_location TEXT, clothing_type TEXT, color_pattern TEXT, fashion_type TEXT);"

INSERT_CLOTHING = "INSERT INTO clothing(name, body_location, clothing_type, color_pattern, fashion_type) VALUES (?, ?, ?, ?, ?);"

GET_ALL_CLOTHES = "SELECT * FROM clothing;"

GET_CLOTHES_BY_NAME = "SELECT * FROM clothing WHERE name = ?;"

GET_COLOR_PATTERN_FOR_CLOTHES = """
SELECT color_pattern FROM clothing
WHERE name = ?
LIMIT 1; """

def connect():
    return sqlite3.connect("clothing_data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_CLOTHING_TABLE)

def add_clothes(connection, name, body_location, clothing_type, color_pattern, fashion_type):
    with connection:
        connection.execute(INSERT_CLOTHING, (name, body_location, clothing_type, color_pattern, fashion_type))

def get_all_clothes(connection):
    with connection:
        return connection.execute(GET_ALL_CLOTHES).fetchall() #fetchall gets us a list of rows returned by database

def get_clothes_by_name(connection, name):
    with connection:
        return connection.execute(GET_CLOTHES_BY_NAME, (name,)).fetchall()
    
def get_color_pattern_for_clothes(connection, name):
    with connection:
        return connection.execute(GET_COLOR_PATTERN_FOR_CLOTHES, (name,)).fetchone()