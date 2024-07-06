import discord
from discord.ext import commands

bot = commands.Bot("/", intents=discord.Intents.all())
with open("token.txt", "r") as file:
    token = file.readline()
    channel_id = int(file.readline())


@bot.event
async def on_ready():
    # print("Hello World! This is Mr. Camel Bot")
    channel = bot.get_channel(channel_id)
    await channel.send("Restarting")


@bot.command()
async def OtoN(ctx, *args):
    x = int(args[0]) / 8
    if len(args) == 2:
        y = int(args[1]) / 8
        coords = str(x) + ", " + str(y)
    else:
        y = int(args[2]) / 8
        coords = str(x) + ", " + args[1] + ", " + str(y)
    await ctx.send("Nether Coords: " + coords)


@bot.command()
async def NtoO(ctx, *args):
    x = int(args[0]) * 8
    if len(args) == 2:
        y = int(args[1]) * 8
        coords = str(x) + ", " + str(y)
    else:
        y = int(args[2]) * 8
        coords = str(x) + ", " + args[1] + ", " + str(y)
    await ctx.send("Nether Coords: " + coords)

if __name__ == "__main__":
    bot.run(token)