from database import db

class Problems():

  @staticmethod
  def find(id):
    db.execute(f"SELECT * from problems WHERE id = {id}")
    result = db.fetchone()

    return result

  @staticmethod
  def all():
    db.execute(f"SELECT * from problems ORDER BY id DESC")
    result = db.fetchall()

    return result