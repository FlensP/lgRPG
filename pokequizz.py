import os.path
import pickle
import random
from datetime import date

import discord
import pokebase as pb
import requests

list_poke = []
pokemon_data = {}
players = {}

colors = {
    "black": "noir", "blue": "bleu", "brown": "marron", "gray": "gris", "green": "vert", "pink": "rose",
    "purple": "violet", "red": "rouge", "white": "blanc", "yellow": "jaune"}

egg_group = {"monster": "Monstrueux", "water1": "Aquatique 1", "bug": "Insectoïde", "flying": "Aérien",
             "ground": "Terrestre", "fairy": "Féerique", "plant": "Végétal", "humanshape": "Humanoïde",
             "water3": "Aquatique 3", "mineral": "Minéral", "indeterminate": "Amorphe", "water2": "Aquatique 2",
             "ditto": "Métamorph", "dragon": "Draconique", "no-eggs": "Inconnu"}
habitat = {
    "cave": "grottes", "forest": "forêts", "grassland": "champs", "mountain": "montagnes", "rare": "rares",
    "rough-terrain": "milieux hostiles", "sea": "mers", "urban": "urbains", "waters-edge": "marécages"}
shape = {
    "ball": "Balle", "squiggle": "Sinueux", "fish": "Poisson", "arms": "Bras", "blob": "Goutte", "upright": "Droit",
    "legs": "Jambes", "quadruped": "Quadrupède", "wings": "Ailes", "tentacles": "Tentacules", "heads": "Têtes",
    "humanoid": "Humanoïde", "bug-wings": "Ailes d'insecte", "armor": "Armure"}
types = {
    "normal": "Normal", "fighting": "Combat", "flying": "Vol", "poison": "Poison", "ground": "Sol", "rock": "Roche",
    "bug": "Insecte", "ghost": "Spectre", "steel": "Acier", "fire": "Feu", "water": "Eau", "grass": "Plante",
    "electric": "Électrik", "psychic": "Psy", "ice": "Glace", "dragon": "Dragon", "dark": "Ténèbres", "fairy": "Fée"}
shape_emo = {
    "Balle": "<:Balle:1189954695792435220>", "Sinueux": "<:Sinueux:1189954734145142914>",
    "Poisson": "<:Poisson:1189954754290405507>", "Bras": "<:Bras:1189954691837202462>",
    "Goutte": "<:Goutte:1189954690465660949>", "Droit": "<:Droit:1189954689245130792>",
    "Jambes": "<:Jambes:1189954686984392704>", "Quadrupède": "<:Quadrupde:1189954685407338598>",
    "Ailes": "<:Ailes:1189954684639785090>", "Tentacules": "<:Tentacules:1189954682366476368>",
    "Têtes": "<:Ttes:1189954679346573462>", "Humanoïde": "<:Humanode:1189954677941469254>",
    "Ailes d'insecte": "<:Ailesdinsecte:1189954676356034632>", "Armure": "<:Armure:1189954674044977222>"
}


class Data:
    def __init__(self):
        self.list_poke = list_poke


def save():
    with open("list_poke", "wb") as file:
        pickle.Pickler(file).dump(Data())


def load():
    global list_poke
    with open("list_poke", "rb") as file:
        data = pickle.Unpickler(file).load()
        list_poke = data.list_poke


def init_file():
    global list_poke
    print("a")
    if not os.path.isfile("list_poke"):
        list_poke = list(range(1, 905))
        random.shuffle(list_poke)
        list_poke.append(date.today())
        save()
    else:
        load()


def init_poke():
    global pokemon_data, players
    players = {}
    i = int((date.today() - list_poke[904]).days)
    i = list_poke[i]
    a = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{i}")
    json_data_sp = a.json()
    a = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    json_data = a.json()
    a = requests.get(f"{json_data_sp['evolution_chain']['url']}")
    json_evo = a.json()
    pokemon_data["name"] = json_data_sp["names"][4]["name"]
    pokemon_data["weight"] = json_data["weight"]
    pokemon_data["height"] = json_data["height"]
    pokemon_data["color"] = colors[json_data_sp["color"]["name"]]
    pokemon_data["shape"] = shape[json_data_sp["shape"]["name"]]
    pokemon_data["capture_rate"] = json_data_sp["capture_rate"]
    pokemon_data["egg_group"] = egg_group[json_data_sp["egg_groups"][0]["name"]]
    if i <= 151:
        gen = 1
    elif i <= 251:
        gen = 2
    elif i <= 386:
        gen = 3
    elif i <= 493:
        gen = 4
    elif i <= 649:
        gen = 5
    elif i <= 721:
        gen = 6
    elif i <= 807:
        gen = 7
    elif i <= 905:
        gen = 8
    else:
        gen = 9
    pokemon_data["gen"] = gen
    if json_data_sp["evolves_from_species"] is None:
        pokemon_data["is_evolved"] = False
    else:
        pokemon_data["is_evolved"] = True
    stats = [json_data["stats"][0]["base_stat"], json_data["stats"][1]["base_stat"], json_data["stats"][2]["base_stat"],
             json_data["stats"][3]["base_stat"], json_data["stats"][4]["base_stat"], json_data["stats"][5]["base_stat"]]
    pokemon_data["stats"] = stats
    poketype = [types[json_data["types"][0]["type"]["name"]]]
    if len(json_data["types"]) > 1:
        poketype.append(types[json_data["types"][1]["type"]["name"]])
    else:
        poketype.append("Aucun")
    pokemon_data["type"] = poketype
    moves = []
    i = 0
    while i < len(json_data["moves"]):
        moves.append(json_data["moves"][i]["move"]["name"])
        i += 1
    random.shuffle(moves)
    i = 0
    while i < len(moves) and i < 15:
        moves[i] = pb.move(moves[i]).names[3].name
        i += 1
    pokemon_data["moves"] = moves
    abilities = []
    i = 0
    while i < len(json_data["abilities"]):
        abilities.append(pb.ability(json_data["abilities"][i]["ability"]["name"]).names[3].name)
        i += 1
    random.shuffle(abilities)
    while len(abilities) < 3:
        abilities.append("Aucun")
    pokemon_data["abilities"] = abilities
    en_name = json_data_sp["name"]
    if len(json_evo["chain"]["evolves_to"]) == 0:
        pokemon_data["can_evolve"] = False
    elif json_evo["chain"]["species"]["name"].lower() == en_name.lower():
        pokemon_data["can_evolve"] = True
    else:
        i = 0
        pokemon_data["can_evolve"] = False
        while i < len(json_evo["chain"]["evolves_to"]):
            if json_evo["chain"]["evolves_to"][i]["species"]["name"].lower() == en_name.lower():
                pokemon_data["can_evolve"] = len(json_evo["chain"]["evolves_to"][i]["evolves_to"]) > 0
            i += 1


class SelectMenu(discord.ui.Select):
    def __init__(self, titre):
        options = [discord.SelectOption(label="type", description="Type du pokémon : 200"),
                   discord.SelectOption(label="génération", description="Génération du pokémon : 100"),
                   discord.SelectOption(label="poids/taille", description="Poids et taille du pokémon : 20"),
                   discord.SelectOption(label="talent", description="Talent du pokémon : 100"),
                   discord.SelectOption(label="attaque", description="Attaque du pokémon : 10"),
                   discord.SelectOption(label="taux de capture", description="Taux de capture du pokémon : 5"),
                   discord.SelectOption(label="info dex", description="Couleur ou forme du pokémon : 40"),
                   discord.SelectOption(label="groupe oeuf", description="Groupe oeuf du pokémon : 15"),
                   discord.SelectOption(label="peut évoluer", description="Si le pokémon peut évoluer : 50"),
                   discord.SelectOption(label="a évolué", description="Si le pokémon a déjà évolué : 70"),
                   discord.SelectOption(label="stat", description="Une stat du pokémon : 15"),
                   discord.SelectOption(label="allstat", description="Toutes les stats du pokémon : 50")]
        super().__init__(placeholder=titre, min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        match self.values[0]:
            case "type":
                players[interaction.user.id]["hints"]["type"] += 1
                players[interaction.user.id]["points"] += 200
            case "génération":
                players[interaction.user.id]["hints"]["gen"] += 1
                players[interaction.user.id]["points"] += 100
            case "poids/taille":
                players[interaction.user.id]["hints"]["w/h"] += 1
                players[interaction.user.id]["points"] += 20
            case "talent":
                players[interaction.user.id]["hints"]["tal"] += 1
                players[interaction.user.id]["points"] += 100
            case "attaque":
                players[interaction.user.id]["hints"]["atk"] += 1
                players[interaction.user.id]["points"] += 10
            case "taux de capture":
                players[interaction.user.id]["hints"]["capt"] += 1
                players[interaction.user.id]["points"] += 5
            case "info dex":
                players[interaction.user.id]["points"] += 40
                if players[interaction.user.id]["hints"]["color"] > 0:
                    players[interaction.user.id]["hints"]["shape"] += 1
                elif players[interaction.user.id]["hints"]["shape"] > 0:
                    players[interaction.user.id]["hints"]["color"] += 1
                elif random.randint(0, 1) > 0:
                    players[interaction.user.id]["hints"]["shape"] += 1
                else:
                    players[interaction.user.id]["hints"]["color"] += 1
            case "groupe oeuf":
                players[interaction.user.id]["hints"]["egg"] += 1
                players[interaction.user.id]["points"] += 15
            case "peut évoluer":
                players[interaction.user.id]["hints"]["can_evo"] += 1
                players[interaction.user.id]["points"] += 50
            case "a évolué":
                players[interaction.user.id]["hints"]["is_evo"] += 1
                players[interaction.user.id]["points"] += 70
            case "stat":
                players[interaction.user.id]["hints"]["stat"] += 1
                players[interaction.user.id]["points"] += 15
            case "allstat":
                players[interaction.user.id]["hints"]["stat"] += 6
                players[interaction.user.id]["points"] += 50
        await edit_embed(interaction)
        await interaction.response.defer()


async def edit_embed(interaction):
    global players
    emb = discord.Embed(title=f"Pokémon du jour", colour=0x9F1E1A)
    emb.set_footer(text="LG Bot by Flens_")
    txt = ""
    hints = players[interaction.user.id]["hints"]
    if hints["gen"] > 0:
        txt += f"La génération du pokémon est : {pokemon_data['gen']}\n"
    if hints["type"] > 0:
        if hints["type"] == 1:
            txt += f"Les types du pokémon sont : {pokemon_data['type'][0]} et ???\n"
        else:
            txt += f"Les types du pokémon sont : {pokemon_data['type'][0]} et {pokemon_data['type'][1]}\n"
    if hints["w/h"] > 0:
        txt += f"Le pokémon fait : {pokemon_data['weight'] / 10}kg et {pokemon_data['height'] / 10}m\n"
    if hints["tal"] > 0:
        txt2 = ""
        for i in range(min(3, hints["tal"])):
            txt2 += f"{pokemon_data['abilities'][i]} "
        txt += f"Le pokémon a comme talent(s) : {txt2}\n"
    if hints['atk'] > 0:
        txt2 = ""
        for i in range(min(len(pokemon_data['moves']), hints["atk"])):
            txt2 += f"{pokemon_data['moves'][i]} "
        txt += f"Le pokémon a comme attaque(s) : {txt2}\n"
    if hints["capt"] > 0:
        txt += f"Le taux de capture du pokémon est de : {pokemon_data['capture_rate']}\n"
    if hints["color"] > 0:
        txt += f"La couleur du pokémon est : {pokemon_data['color']}\n"
    if hints["shape"] > 0:
        txt += f"La forme du pokémon est : {pokemon_data['shape']} {shape_emo[pokemon_data['shape']]}\n"
    if hints["egg"] > 0:
        txt += f"Le groupe oeuf du pokémon est : {pokemon_data['egg_group']}\n"
    if hints["can_evo"] > 0:
        if pokemon_data['can_evolve']:
            txt += "Le pokémon peut évoluer\n"
        else:
            txt += "Le pokémon ne peut pas évoluer\n"
    if hints["is_evo"] > 0:
        if pokemon_data['is_evolved']:
            txt += "Le pokémon a déjà évolué\n"
        else:
            txt += "Le pokémon n'a pas déjà évolué\n"
    if hints['stat'] > 0:
        txt2 = ""
        for i in range(min(6, hints["stat"])):
            txt2 += f"{pokemon_data['stats'][i]} "
        txt += f"Le pokémon a comme stat(s) : {txt2}\n"
    emb.add_field(name="Indices:", value=txt, inline=False)
    emb.add_field(name="Score:", value=players[interaction.user.id]["points"], inline=False)
    await players[interaction.user.id]["message"].edit(embed=emb)


class QuizzView(discord.ui.View):
    def __init__(self, timeout, user):
        super().__init__(timeout=timeout)
        self.add_item(SelectMenu("Demande un indice"))

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

    async def on_timeout(self) -> None:
        await self.disable_all_items()


async def play(ctx, client):
    global players
    if ctx.user.id not in players:
        players[ctx.user.id] = {"points": 0,
                                "hints": {"type": 0, "gen": 0, "w/h": 0, "tal": 0, "atk": 0, "capt": 0, "color": 0,
                                          "shape": 0,
                                          "egg": 0, "can_evo": 0, "is_evo": 0, "stat": 0}, "find": False,
                                "message": None}
    if players[ctx.user.id]["find"]:
        await ctx.response.send_message(
            f"Vous avez déjà trouvé le pokémon du jour {pokemon_data['name']} avec un score de : {players[ctx.user.id]['points']}")
        return
    if not ctx.channel.type == discord.ChannelType.private:
        await ctx.response.send_message(
            f"Vous devez vous rendre en message privé pour jouer")
        return
    await ctx.response.send_message(
        "L'objectif est de trouver le pokémon du jour avec le plus petit score possible. Pour faire une tentative, "
        "utilisez la commande /guess avec le nom en français du pokémon dans ce channel (chaque essai donnera 5 "
        "point s'il est faux). Amusez vous bien !")
    emb = discord.Embed(title=f"Pokémon du jour", colour=0x9F1E1A)
    emb.set_footer(text="LG Bot by Flens_")
    view = QuizzView(timeout=1200, user=ctx.user)
    chan = await ctx.user.create_dm()
    players[ctx.user.id]["message"] = await chan.send(embed=emb, view=view)
    view.message = players[ctx.user.id]["message"]
    await edit_embed(ctx)
    await view.wait()
    await view.disable_all_items()


async def guess(ctx, client, name):
    global players, pokemon_data
    if ctx.user.id not in players:
        await ctx.response.send_message(
            f"Vous n'avez pas encore commencé le pokequizz du jour, faites /pokequizz pour débuter !")
        return
    if players[ctx.user.id]["find"]:
        await ctx.response.send_message(
            f"Vous avez déjà trouvé le pokémon du jour {pokemon_data['name']} avec un score de : {players[ctx.user.id]['points']}")
        return
    if not ctx.channel.type == discord.ChannelType.private:
        await ctx.response.send_message(
            f"Vous devez vous rendre en message privé pour jouer")
        return
    if name.lower() == pokemon_data["name"].lower():
        await ctx.response.send_message(
            f"Vous avez trouvé ! GG à vous")
        players[ctx.user.id]['find'] = True
        return
    else:
        await ctx.response.send_message(f"Mauvaise réponse (faites attention à l'orthographe !) + 5 points")
        players[ctx.user.id]['points'] += 5
