import discord
from discord.ext import commands

bot = commands.Bot("/", intents=discord.Intents.all())
with open("token.txt", "r") as file:
    token = file.readline()
    channel_id = int(file.readline())


@bot.event
async def on_ready():
    print("Hello World! This is Mr. Camel Bot")
    channel = bot.get_channel(channel_id)
    await channel.send("Bot is alive!")


if __name__ == "__main__":
    bot.run(token)