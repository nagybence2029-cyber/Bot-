import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"A bot elindult! Bejelentkezve mint: {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


# IDE MÁSOLD A SAJÁT BOT TOKENEDET AZ IDŐZŐJELEK KÖZÉ:
TOKEN = "MTU0Njg5MzQ1MTk4MTc1MDMwNA.G_vPOC.JJzldoxFJtdsDopo-KVYRTHVhyHQwN2ORRnOLg"

print("Indítás...")
bot.run(TOKEN)
