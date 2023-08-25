from database import db
from which import which_column_problems, which_column_competitor, which_column_solution
from models.competitor import Competitor

class CompetitorSolution:

  @staticmethod
  def find(problem_id, user_id):
    db.execute(f"SELECT * from users_solution WHERE problem = {problem_id} AND user = {user_id}")
    solution = db.fetchone()

    return solution

  @staticmethod
  def create(problem_id, user_id, solution):
    db.execute(f"SELECT * from users_solution WHERE problem = {problem_id} AND user = {user_id}")
    solution_exists = db.fetchone()

    if not solution_exists:
      fetch_user = Competitor.get_user_by_id(user_id)

      db.execute(f"INSERT INTO users_solution(problem, user, solution) VALUES({problem_id}, {user_id}, '{solution}')")
      db.execute(f"UPDATE users SET points = {fetch_user[which_column_competitor('points')] + 5} WHERE id = {fetch_user[which_column_competitor()]}")

      return True
    else:
      return False