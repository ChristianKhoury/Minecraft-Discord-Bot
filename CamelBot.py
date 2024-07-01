import discord
from discord.ext import commands

bot = commands.Bot("/", intents=discord.Intents.all())


class CamelBot:
    def __init__(self, bot):
        self.token = None
        self.channel = None
        self.bot = bot

        self.init_token()

        self.bot.run(self.token)
    

    def init_token(self):
        with open("token.txt", "r") as file:
            self.token = file.readline()
            channel_id = int(file.readline())
            self.channel = self.bot.get_channel(channel_id)


@bot.event
async def on_ready():
    print("Hello World! This is Mr. Camel Bot")



if __name__ == "__main__":
    CamelBot(bot)
