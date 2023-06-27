import discord
import numpy as np

replies = [
    'Peut être',
    'Sûrement pas.',
    "Je l'espère.",
    'Même pas dans vos rêves les plus fous.',
    'Il y a une grande chance.',
    'Un truc du genre.',
    'Je le pense.',
    "J'espère que non.",
    'Jamais!',
    'Pfft.',
    'Déso pas déso.',
    'Malheureusement, oui.',
    "Sur l'enfer, non",
    'Le futur nous le dira .',
    "Rien n'est moins sûr.",
    'Je préfère ne pas le dire.',
    'Qui est intéressé par cette question ? ^^',
    'Sûrement.',
    'Jamais, jamais, jamais.',
    'Il y a une petite chance.',
    'Oui !',
    'lol non.',
    'Il y a une grande chance.',
    "Qu'est-ce que ça change?",
    'Pas mon soucis.',
    "Demande à quelqu'un d'autre.",
    "M'en bats les couilles frère",
    "Le Grand Flens possède la réponse",
    "Des frites avec de la mayo svp",
    "Même Stephen n'est pas aussi con que cette question",
    "Tu veux une épée sharpness II dans ta gueule ?",
    "Tu m'as dérangé pour me poser cette question ? Sérieusement ?",
    "JE TE PISSE À LA RAIE !",
    "Ratio."
]


async def avis(question):
    emb = discord.Embed(title="AVIS !", colour=0x9F1E1A)
    emb.set_footer(text="LG RPG by Flens_")
    emb.add_field(name="Question:", value=question, inline=False)
    np.random.shuffle(replies)
    emb.add_field(name="Réponse:", value=replies[0], inline=False)
    return emb
