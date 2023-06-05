import random
from avis import avis

import discord


def commands_list(client, tree):
    # Make the roll command
    @tree.command(name="roll", description="Roll a die")
    async def die_roll(interaction: discord.Interaction):
        await interaction.response.send_message(f"{random.randint(1, 6)} \N{GAME DIE}")

    # Make the ping command
    @tree.command(name="ping", description="Test the ping of the bot")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! In {round(client.latency * 1000)}ms")

    # Make a cheh command
    @tree.command(name="cheh", description="Cheh somebody")
    async def cheh(interaction: discord.Interaction, user: discord.Member):
        # Check if the user to cheh is the bot or the user sending the command
        if user == client.user:
            await interaction.response.send_message("Vous ne pouvez pas me **Cheh** !")
        elif user == interaction.user:
            await interaction.response.send_message("**FEUR**")
        else:
            cheh_gif = "https://tenor.com/view/cheh-true-cheh-gif-19162969"
            await interaction.response.send_message(f"Cheh {user.mention}")
            await interaction.channel.send(cheh_gif)

    @tree.command(name="avis", description="Donne son avis")
    async def avis2(interaction: discord.Interaction, question: str):
        await interaction.response.send_message(embed=await avis(question))

    # Make a simple context menu application
    @tree.context_menu(name="Hello")
    async def hello(interaction: discord.Interaction, message: discord.Message):
        await interaction.response.send_message(f"Hey! {interaction.user.mention}")

