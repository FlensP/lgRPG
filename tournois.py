import datetime

import discord

tournois = []
fr = []


async def send_message(client):
    flens = client.get_user(309331967382519819)
    chan = await flens.create_dm()
    emb = discord.Embed(title=f"Tournois VGC FR", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    for t in fr:
        txt = f"nom = {t[4]}\nLocalisation : {t[3]}"
        emb.add_field(name=f"Tournoi à {t[1]} le {t[5].day}/{t[5].month}/{t[5].year}", value=txt, inline=False)
    await chan.send(embed=emb)


async def filter_tournois():
    global fr
    fr = []
    for t in tournois:
        if t[2] == "FR":
            fr.append(t)
    for t in fr:
        date = t[5][:10]
        date = date.split("-")
        t[5] = datetime.datetime(date[0], date[1], date[2])
    fr.sort(key=lambda x: x[5])
