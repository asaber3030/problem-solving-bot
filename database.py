import mysql.connector as connect

from config import DB_NAME, DB_HOST, DB_PASSWORD, DB_USERNAME

c = connect.connect(
  host=DB_HOST,
  username=DB_USERNAME,
  password=DB_PASSWORD,
  database=DB_NAME
)

db = c.cursor()

def which_column(column='id') -> int:
  if column == 'id':
    return 0
  elif column == 'name':
    return 1
  elif column == 'username':
    return 2
  elif column == 'points':
    return 3
  elif column == 'joined_at':
    return 4
  elif column == 'tag':
    return 5


class competitor():

  @staticmethod
  def get_user_by_id(id: int) -> tuple:
    db.execute(f"SELECT * from users WHERE id = {id}")
    result = db.fetchone()
    return result

  @staticmethod
  def get_user_by_username(us: str) -> tuple:
    db.execute(f"SELECT * from users WHERE username = '{us}'")
    result = db.fetchone()
    return result

  @staticmethod
  def get_user_rank(id: int) -> int:
    db.execute(f"SELECT * from users ORDER BY points DESC")
    competitors = db.fetchall()

    rank = 0

    for index, row in enumerate(competitors):
      if row[which_column('id')] == id:
        rank = index + 1

    return rank

  @staticmethod
  def get_user_points(username: str) -> int:
    db.execute(f"SELECT * from users where username = '{username}'")
    competitor = db.fetchone()

    return competitor[which_column('points')]
