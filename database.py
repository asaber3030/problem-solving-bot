import mysql.connector as connect

from config import DB_NAME, DB_HOST, DB_PASSWORD, DB_USERNAME

c = connect.connect(
  host=DB_HOST,
  username=DB_USERNAME,
  password=DB_PASSWORD,
  database=DB_NAME
)

db = c.cursor()




