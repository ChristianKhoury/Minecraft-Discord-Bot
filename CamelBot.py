from discord.ext import commands


def init_token():
    with open("token.txt", "r") as file:
        token = file.read()
    return token

if __name__ == "__main__":
    print(init_token())