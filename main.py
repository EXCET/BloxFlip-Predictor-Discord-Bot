import discord
from discord.ext import commands
import random




prefix = "RNG "

token = "A"

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command()
async def crash(ctx):
  percent999 = random.randint(1, 99)
  r1 = random.randint(1, 4)
  r2 = random.randint(1, 99)
  embed = discord.Embed(title="RNG PREDICTOR", description=f"{r1}.{r2}\n{percent999}%")
  await ctx.send(embed=embed)

@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command()
async def towers(ctx, towersid):
  percent999 = random.randint(1, 100)
  r1 = random.randint(1, 3)
  r3 = random.randint(1, 3)
  r2 = random.randint(1, 3)
  if r1 == 1:
    place1 = ":star:"
  if r1 == 2:
    place1 = ":x:"
  if r1 == 3:
    place1 = ":x:"
  if r2 == 1:
    place2 = ":star:"
  if r2 == 2:
    place2 = ":x:"
  if r2 == 3:
    place2 = ":x:"
  if r3 == 1:
    place3 = ":star:"
  if r3 == 2:
    place3 = ":x:"
  if r3 == 3:
    place3 = ":x:"
  embed = discord.Embed(title="RNG PREDICTOR", description=f"{place1} {place2} {place3}\n{percent999}%")
  await ctx.send(embed=embed)


@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command()
@commands.has_role('Beta Tester')
async def minesbeta(ctx, id, amount):
  r1 = random.randint(1, 6)
  if r1 == 1:
   embed = discord.Embed(title="RNG PREDICTOR", description=f"Mines Amount: {amount}\n:white_check_mark::question::question::question::question:\n:question::question::question::question::question:\n:white_check_mark::question::question::white_check_mark::question:\n:question::question::question::question::question:\n:question::question::question::question::white_check_mark:")
   await ctx.author.send(embed=embed)
   await ctx.send('Sent Prediction To Dms')
  if r1 == 2:
    embed = discord.Embed(title="RNG PREDICTOR", description=f"Mines Amount: {amount}\n:question::question::question::question::white_check_mark:\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::white_check_mark::question::question::question:\n:question::white_check_mark::question::question::question:")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent Prediction To Dms')
  if r1 == 3:
    embed = discord.Embed(title="RNG PREDICTOR", description=f"Mines Amount: {amount}\n:question::question::question::question::white_check_mark:\n:question::question::question::question::white_check_mark:\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::white_check_mark::question::question::white_check_mark:")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent Prediction To Dms')
  if r1 == 4:
    embed = discord.Embed(title="RNG PREDICTOR", description=f"Mines Amount: {amount}\n:question::question::question::question::white_check_mark:\n:question::question::question::question::white_check_mark:\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::question::question::question::white_check_mark:")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent Prediction To Dms')
  if r1 == 5:
    embed = discord.Embed(title="RNG PREDICTOR", description=f"Mines Amount: {amount}\n:white_check_mark::question::question::question::question:\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::question::question::question::white_check_mark:")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent Prediction To Dms')
  if r1 == 6:
    embed = discord.Embed(title="RNG PREDICTOR", description=f"Mines Amount: {amount}\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::question::question::question::question:\n:question::question::question::question::white_check_mark:")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent Prediction To Dms')

@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command()
async def roulette(ctx):
  r1 = random.randint(1, 2)
  if r1 == 1:
    predi = "2X:purple_square:"
  if r1 == 2:
    predi = "2X:red_square:"
  embed = discord.Embed(title="RNG PREDICTOR", description=f"{predi}")
  await ctx.send(embed=embed)


bot.run(token)
