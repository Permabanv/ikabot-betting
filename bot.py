import discord, pickle
from discord.ext import commands, tasks
from itertools import cycle
import os

os.chdir('c:/Users/Quentin/Desktop')

TOKEN ='NzI5MDkwOTQyNDYzNzcwNzM0.XwENQw.arITbYjfazPDxzNd_EQ6HFlhQ-E'
client = commands.Bot(command_prefix = '!') 
status = cycle(['Développé par Permaban', 'Assisté par Epidemia', 'Bientôt disponible !'])

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

@client.command()
async def register(ctx, joueur, *activité): # Sert à consulter les inscrits à une activité
    with open ('participants', 'rb') as fich_reg:
        register = pickle.load(fich_reg, encoding='bytes')
    register.append(joueur)

    with open('participants','wb') as fich_reg:
         pickle.dump(register, fich_reg)

    await ctx.send('Votre inscription pour {} à bien été prise en compte.')

@client.command()
async def bet(ctx, joueur, bois=0, marbre=0, vin=0, cri=0, s=0):
    with open('registre', 'rb') as fich_reg:
        bets = pickle.load(fich_reg, encoding='bytes')  
    bets.append((joueur, [bois, marbre, vin, cri, s])) # On ajoute le bet actuel à la liste existante

    with open('registre', 'wb') as fich_reg:
        pickle.dump(bets, fich_reg)
    
    await ctx.send("Vous avez bien misé {} bois, {} marbre, {} vin, {} cristal, {} soufre sur {}.".format(bois, marbre, vin, cri, s, joueur))

def int_list(L):
    L = []
    for x in L:
        L.append(int(x))
    return L

@client.command()
async def current_bets(ctx): # Sert à consulter les bets existants
    with open('registre', 'rb') as fich_reg:
        bets = pickle.load(fich_reg, encoding='bytes')
    await ctx.send("== Liste des Paris en cours== \n Format : \n Joueur - [Bois, Marbre, Vin, Cristal, Soufre]")
    for bet in bets:
        await ctx.send("{} - {}".format(bet[0], bet[1]))

@client.command()
async def clear_bets(ctx): # Efface la liste des paris posés VERIFIER LES AUTORISATIONS DES QUE POSSIBLE
    with open('registre', 'wb') as fich_reg:
        empty_list = []
        pickle.dump(empty_list, fich_reg)
    await ctx.send('Registre des bets vidé.')
    

client.run(TOKEN)
