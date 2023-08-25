def which_column_problems(col = 'id'):
  if col == 'id':
    return 0
  elif col == 'title':
    return 1
  elif col == 'content':
    return 2
  elif col == 'type':
    return 3
  elif col == 'url':
    return 4
  elif col == 'created_at':
    return 5

def which_column_competitor(column='id') -> int:
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

def which_column_solution(column='id') -> int:
  if column == 'id':
    return 0
  elif column == 'problem':
    return 1
  elif column == 'user':
    return 2
  elif column == 'solution':
    return 3
  elif column == 'created_at':
    return 4
