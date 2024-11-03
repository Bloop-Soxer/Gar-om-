import discord
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN', '123')

bot = discord.Bot()

@bot.command(description="Faz um pedido")
async def pedido(ctx):
    await ctx.respond("Falae meu chegado! Qual o seu pedido? 🫡")


bot.run(TOKEN)
