import discord

from discord.ext import commands
from constants import TOKEN
from helpers import divider
from database import competitor, db, which_column

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def users(ctx):
  msg = ""
  await ctx.send(msg)

@client.command()
async def rank(ctx):
  auth = ctx.message.author

  get_user = competitor.get_user_by_username(ctx.message.author)
  get_rank = competitor.get_user_rank(get_user[which_column('id')])

  await ctx.send(f"Your Current Rank is **[{get_rank}]** As: **[{get_user[which_column('name')]}]**")

@client.command()
async def points(ctx):
  auth = ctx.message.author
  get_user = competitor.get_user_by_username(ctx.message.author)

  await ctx.send(f"Your Current Points is **[{get_user[which_column('points')]}]** As: **[{get_user[which_column('name')]}]**")

@client.command()
async def points(ctx):
  auth = ctx.message.author
  get_user = competitor.get_user_by_username(ctx.message.author)

  await ctx.send(f"Your Current Points is **[{get_user[which_column('points')]}]** As: **[{get_user[which_column('name')]}]**")

client.run(TOKEN)