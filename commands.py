import random
import game
import discord
import idea
import autorisation
from avis import avis


def commands_list(client, tree):
    @tree.command(name="roll", description="Roll a die")
    async def die_roll(interaction: discord.Interaction):
        await interaction.response.send_message(f"{random.randint(1, 6)} \N{GAME DIE}")

    @tree.command(name="ping", description="Test the ping of the bot")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! In {round(client.latency * 1000)}ms")

    @tree.command(name="game", description="Organise une partie de LG")
    async def game2(interaction: discord.Interaction):
        await game.run(interaction, client)

    @tree.command(name="autorisation", description="Donne ou demande l'autorisation pour faire une game")
    async def auto(interaction: discord.Interaction, user: discord.Member):
        await autorisation.run(interaction, client, user)

    @tree.command(name="cheh", description="Cheh somebody")
    async def cheh(interaction: discord.Interaction, user: discord.Member):
        # Check if the user to cheh is the bot or the user sending the command
        if user == client.user:
            await interaction.response.send_message("Vous ne pouvez pas me **Cheh** !")
        elif user.id == 309331967382519819:
            await interaction.response.send_message(f"Tu ne peux pas cheh dieu {interaction.user.mention}")
        elif user == interaction.user:
            await interaction.response.send_message("**FEUR**")
        else:
            cheh_gif = "https://tenor.com/view/cheh-true-cheh-gif-19162969"
            await interaction.response.send_message(f"Cheh {user.mention}")
            await interaction.channel.send(cheh_gif)

    @tree.command(name="avis", description="Demande l'avis au bot")
    async def avis2(interaction: discord.Interaction, question: str):
        await interaction.response.send_message(embed=await avis(question))


    @tree.command(name="proposition", description="Fait une proposition d'amélioration pour le bot")
    async def proposition(interaction: discord.Interaction, proposition: str):
        await idea.run(interaction, proposition, client)

    @tree.context_menu(name="Hello")
    async def hello(interaction: discord.Interaction, message: discord.Message):
        await interaction.response.send_message(f"Hey! {interaction.user.mention}")
