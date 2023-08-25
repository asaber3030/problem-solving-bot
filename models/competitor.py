from database import db
from which import which_column_competitor

class Competitor:

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
      if row[which_column_competitor('id')] == id:
        rank = index + 1

    return rank

  @staticmethod
  def get_user_points(username: str) -> int:
    db.execute(f"SELECT * from users where username = '{username}'")
    competitor = db.fetchone()

    return competitor[which_column_competitor('points')]

  @staticmethod
  def get_ranks_ordered():
    db.execute(f"SELECT * from users ORDER BY points DESC")
    users = db.fetchall()

    return users

