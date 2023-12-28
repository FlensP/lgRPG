import datetime

import discord

tournois = []
fr = []
be = []
de = []
gb = []
lu = []
nl = []
ch = []
it = []
majors = {'Régional de Liverpool': datetime.date(2024, 1, 27), 'Régional de Dortmund': datetime.date(2024, 2, 10),
          "Spécial d'Utrecht": datetime.date(2024, 3, 2), 'EUIC à Londres': datetime.date(2024, 4, 5),
          'Régional de Stockholm': datetime.date(2024, 5, 11)}


async def send_message(client):
    chan = client.get_channel(1132311114135371827)
    emb = discord.Embed(title=f"Tournois VGC FR", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    for t in fr:
        txt = f"nom = {t[4]}"
        emb.add_field(name=f"Tournoi à {t[0]} le {t[5].day}/{t[5].month}/{t[5].year}", value=txt, inline=False)
    await chan.send(embed=emb)
    emb = discord.Embed(title=f"Tournois VGC BE", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    for t in be:
        txt = f"nom = {t[4]}"
        emb.add_field(name=f"Tournoi à {t[0]} le {t[5].day}/{t[5].month}/{t[5].year}", value=txt, inline=False)
    await chan.send(embed=emb)
    emb = discord.Embed(title=f"Tournois VGC CH", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    for t in ch:
        txt = f"nom = {t[4]}"
        emb.add_field(name=f"Tournoi à {t[0]} le {t[5].day}/{t[5].month}/{t[5].year}", value=txt, inline=False)
    await chan.send(embed=emb)
    emb = discord.Embed(title=f"Tournois VGC LU", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    for t in lu:
        txt = f"nom = {t[4]}"
        emb.add_field(name=f"Tournoi à {t[0]} le {t[5].day}/{t[5].month}/{t[5].year}", value=txt, inline=False)
    await chan.send(embed=emb)
    emb = discord.Embed(title=f"Tournois Majeurs", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    today = datetime.date.today()
    for tour in majors.keys():
        emb.add_field(name=f"{tour}", value=f"Dans {(majors[tour] - today).days} jours", inline=False)
    await chan.send(embed=emb)


async def filter_tournois():
    global fr, lu, ch, be, de, gb, nl, it
    fr.clear()
    lu.clear()
    ch.clear()
    be.clear()
    de.clear()
    gb.clear()
    nl.clear()
    it.clear()
    for t in tournois:
        match t[2]:
            case "FR":
                fr.append(t)
            case "LU":
                lu.append(t)
            case "CH":
                ch.append(t)
            case "BE":
                be.append(t)
            case "DE":
                de.append(t)
            case "GB":
                gb.append(t)
            case "NL":
                nl.append(t)
            case "IT":
                it.append(t)
    for t in fr:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    for t in lu:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    for t in ch:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    for t in be:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    for t in de:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    for t in gb:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    for t in nl:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    for t in it:
        date = str(t[5])[:10]
        date = date.split("-")
        t[5] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    fr = [i for n, i in enumerate(fr) if i not in fr[:n]]
    lu = [i for n, i in enumerate(lu) if i not in lu[:n]]
    ch = [i for n, i in enumerate(ch) if i not in ch[:n]]
    be = [i for n, i in enumerate(be) if i not in be[:n]]
    de = [i for n, i in enumerate(de) if i not in de[:n]]
    gb = [i for n, i in enumerate(gb) if i not in gb[:n]]
    nl = [i for n, i in enumerate(nl) if i not in nl[:n]]
    it = [i for n, i in enumerate(it) if i not in it[:n]]
    fr.sort(key=lambda x: x[5])
    lu.sort(key=lambda x: x[5])
    ch.sort(key=lambda x: x[5])
    be.sort(key=lambda x: x[5])
    de.sort(key=lambda x: x[5])
    gb.sort(key=lambda x: x[5])
    nl.sort(key=lambda x: x[5])
    it.sort(key=lambda x: x[5])
