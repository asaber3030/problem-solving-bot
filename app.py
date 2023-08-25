import discord

from discord.ext import commands
from constants import TOKEN
from which import which_column_competitor, which_column_problems, which_column_solution
from models.competitor import Competitor
from models.problem import Problems
from models.competitor_solution import CompetitorSolution

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.command()
async def rank(ctx):
  auth = ctx.message.author

  get_user = Competitor.get_user_by_username(ctx.message.author)
  get_rank = Competitor.get_user_rank(get_user[which_column_competitor('id')])

  await ctx.send(f"Your Current Rank is **[{get_rank}]** As: **[{get_user[which_column_competitor('name')]}]**")

@client.command()
async def points(ctx):
  auth = ctx.message.author
  get_user = Competitor.get_user_by_username(ctx.message.author)

  await ctx.send(
    f"Your Current Points is **[{get_user[which_column_competitor('points')]}]** As: **[{get_user[which_column_competitor('name')]}]**")

@client.command()
async def ranks(ctx):
  comps = Competitor.get_ranks_ordered()
  msg = ""

  for index, comp in enumerate(comps):
    msg += f"**[ {index + 1} ]**. {comp[which_column_competitor('name')]} | Points: **{comp[which_column_competitor('points')]}** \n"

  await ctx.send(msg)

@client.command()
async def get(ctx, select, idx: int):
  problems_channel = client.get_channel(1142814625876951081)
  solutions_channel = client.get_channel(1142814653680984066)

  if select == 'problem':
    if type(idx) == int:
      problem = Problems.find(idx)
      if problem:
        await problems_channel.send(f"Problem Title: **{problem[which_column_problems('title')]}**\nProblem ID: **{problem[which_column_problems('id')]}**\nProblem Type: **{problem[which_column_problems('type')]}**\nURL: **{problem[which_column_problems('url')]}**\n\n{problem[which_column_problems('content')]}")
      else:
        await problems_channel.send(f"No Problem found with this ID: **{idx}**")
    else:
      await problems_channel.send("Error! Cannot accepts other data types in command `/get {select_type} {problem_id}`")

  elif select == 'solution':
    if type(idx) == int:
      username = ctx.message.author
      find_user = Competitor.get_user_by_username(username)
      solution = CompetitorSolution.find(idx, find_user[which_column_competitor()])

      if solution:
        await solutions_channel.send(f"**Solution Found**\nHere's your link: {solution[which_column_solution('url')]}")
      else:
        await solutions_channel.send(f"No solution found to this problem belongs to you! :( `Searching ID: {idx}`")

    else:
      await problems_channel.send("Error! Cannot accepts other data types in command `/get {select_type} {problem_id}`")

  else:
    await problems_channel.send("Error! Unknown select type please make sure to read docs!")

@client.command()
async def answer(ctx, idx, solution):

  submissions_channel = client.get_channel(1142814680050573313)

  get_current_user = Competitor.get_user_by_username(ctx.message.author)
  create_sol = CompetitorSolution.create(idx, get_current_user[which_column_competitor()], solution)

  print(create_sol)

  if create_sol:
    await submissions_channel.send(f"Your solution has been submitted! your new points is {get_current_user[which_column_competitor('points')] + 5}")
  else:
    await submissions_channel.send("Solution already exists!")



client.run(TOKEN)
