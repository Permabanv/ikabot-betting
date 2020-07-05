import discord
from discord.ext import commands, tasks
from itertools import cycle

TOKEN ='NzI5MDkwOTQyNDYzNzcwNzM0.XwENQw.arITbYjfazPDxzNd_EQ6HFlhQ-E'
client = commands.Bot(command_prefix = '!') 
status = cycle(['Développé par Permaban','Bientôt disponible !','Le pari sur Ikariam à portée de main'])

@client.event
async def on_ready():
    change_status.start()
    print('LE BOT EST PRÊT YALAH') 


@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def infos(ctx):
    await ctx.send('Utilisez la commande !bet suivi du nom du participant pour ajouter des ressources. Chaque palier de 10000 ressources baisse la côte du joueur visé')

client.run(TOKEN)
