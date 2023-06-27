import json
import random

import discord

roles = ["loup garou", "voyante", "sorcière", "simple villageois", "cupidon", "chasseur", "voleur", "salvateur",
         "idiot du village", "bouc émissaire", "ange", "loup garou blanc", "prostituée", "corbeau", "grand Manitou",
         "infect père des loups", "enfant sauvage", "isolateur", "détective", "soeur", "citoyen", "grand méchant loup",
         "loup feutré", "renard", "montreur d'ours", "ancien", "chevalier à l'épée rouillée", "villageois-villageois",
         "chien-loup", "trublion", "arnacoeur", "avocat", "ankou", "juge bègue", "facteur", "assassin",
         "servante dévouée", "comédien", "loup bavard", "cupidon maudit", "charmeuse"]
roles_loup = ["loup garou", "loup garou blanc", "infect père des loups", "grand méchant loup", "loup feutré",
              "loup bavard"]
joueurs = []
roles_list = []
desc = json.load(open("ress/roles.json", encoding='utf-8'))
color = json.load(open("ress/color.json", encoding='utf-8'))
message = None
guild = None


class SelectMenu(discord.ui.Select):
    def __init__(self, titre, max, list):
        options = [discord.SelectOption(label=role, description=f"Ajouter un.e {role}") for role in list]
        super().__init__(placeholder=titre, min_values=1, max_values=max, options=options)

    async def callback(self, interaction: discord.Interaction):
        roles_list.extend(self.values)
        await edit_embed(interaction)


class SimpleView(discord.ui.View):
    def __init__(self, timeout):
        super().__init__(timeout=timeout)
        i = 0
        while i <= len(roles):
            max = min(len(roles) - 1, i + 24)
            self.add_item(SelectMenu("Ajouter un rôle", len(roles[i:max]), roles[i:max]))
            i += 25

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

    async def on_timeout(self) -> None:
        await self.disable_all_items()

    @discord.ui.button(label="Envoyer les rôles",
                       style=discord.ButtonStyle.success)
    async def send(self, interaction: discord.Interaction, button: discord.ui.Button):
        if len(joueurs) == len(roles_list):
            loups = await send_roles(interaction.user)
            await create_foret(loups)
        else:
            await interaction.response.send_message("Il n'y a pas le même nombre de rôles et de joueurs")

    @discord.ui.button(label="Supprimer les rôles",
                       style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        roles_list.clear()
        await edit_embed(interaction)


async def edit_embed(interaction):
    global message
    emb = discord.Embed(title=f"Compo pour {len(joueurs)}", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    roles_list.sort()
    txt = ""
    for i in range(len(roles_list)):
        txt += f"{roles_list[i]}\n"
    emb.add_field(name="Roles:", value=txt, inline=False)
    await message.edit(embed=emb)


async def send_roles(user):
    global joueurs, roles_list, roles_loup
    random.shuffle(joueurs)
    loups = [user]
    txt = "Compo de la partie :\n"
    for i in range(len(joueurs)):
        emb = discord.Embed(title="Votre rôle", colour=int(color[roles_list[i]], 16))
        emb.set_footer(text="LG RPG by Flens_")
        emb.add_field(name="Vous êtes:", value=f"**{roles_list[i]}**", inline=True)
        emb.add_field(name="Description:", value=desc[roles_list[i]], inline=False)
        chan = await joueurs[i].create_dm()
        await chan.send(embed=emb)
        txt += f"{roles_list[i]} : {joueurs[i].name}\n"
        if roles_list[i] in roles_loup:
            loups.append(joueurs[i])
    chan = await user.create_dm()
    await chan.send(txt)
    return loups


async def create_foret(loups):
    global guild
    cat = discord.utils.get(guild.categories, id=390962605306675204)
    chan = await guild.create_text_channel("🌲・forêt", category=cat)
    await chan.set_permissions(guild.default_role, read_messages=False)
    for loup in loups:
        await chan.set_permissions(loup, read_messages=True)


async def run(ctx):
    global message, joueurs, guild
    ids = [309331967382519819, 229282075918729216, 272123414527868928, 337996843277615107]
    if ctx.user.id not in ids:
        await ctx.response.send_message("Vous devez avoir les perms pour jouer")
        return
    if ctx.user.voice is None:
        await ctx.response.send_message("Vous devez être en voc pour jouer")
        return
    channel = ctx.user.voice.channel
    guild = channel.guild
    joueurs = channel.members
    joueurs.remove(ctx.user)
    if len(joueurs) == 0:
        await ctx.response.send_message("Vous devez avoir des joueurs pour jouer")
        return
    ctx.response.send_message("Passons en mp")
    view = SimpleView(timeout=120)
    emb = discord.Embed(title=f"Compo pour {len(joueurs)}", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    chan = await ctx.user.create_dm()
    message = await chan.send(embed=emb, view=view)
    view.message = message
    await view.wait()
    await view.disable_all_items()
