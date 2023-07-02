import game
from datetime import datetime


async def run(ctx, client, user):
    if str(ctx.user.id) not in client.config['PERMS'].split():
        chan = client.get_channel(int(client.config['AUTO_CHAN']))
        await chan.send(f"Demande d'autorisation de partie de {ctx.user.name}")
        await ctx.response.send_message("Demande effectuée")
    else:
        game.autorisations[user] = datetime.now()
        await ctx.response.send_message(f"{user.name} a été autorisé a faire une partie pour la prochaine heure")
