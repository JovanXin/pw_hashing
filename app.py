import bcrypt
from database_connection import DatabaseConnection

def create_table():
  with DatabaseConnection("data.db") as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS validation(username text primary key,password text)')

def add_username_password():
    hashed_password = bcrypt.hashpw(input("Enter your password").encode("utf-8"), bcrypt.gensalt())
    username = input("Enter your username")
    print(hashed_password)
    with DatabaseConnection("data.db") as connection:
      cursor = connection.cursor()
      cursor.execute('INSERT INTO validation VALUES(?,?)',(username,hashed_password))


# Hash a password for the first time, with a randomly-generated salt

def print_columns():
  with DatabaseConnection("data.db") as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM validation')
    print([row for row in cursor.fetchall()])

def fetch_password():
  username = input("Enter username to fetch from")
  with DatabaseConnection("data.db") as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM validation WHERE username=?',(username,))
    return [row for row in cursor.fetchall()]

def validate_password():
  datas = fetch_password()
  for data in datas:
    print(data)
    password = data[1]
    print(password)
    if bcrypt.checkpw((input("enter your password").encode("utf-8")), password):
      print("VALIDATED")
    else:
      print("DENIED")


if __name__ == "__main__":
  create_table()
  while True:
    option = input("Enter your option")
    if option == "a":
      add_username_password()
    elif option == "p":
      print_columns()
    elif option == "f":
      fetch_password()
    elif option == "v":
      validate_password()
