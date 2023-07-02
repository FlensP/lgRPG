async def run(ctx, proposition, client):
    chan = client.get_channel(int(client.config['IDEA_CHAN']))
    await chan.send(f"Proposition de {ctx.user.name} : {proposition}")
    await ctx.response.send_message("La proposition a été soumise. Attention, les abus seront sanctionnés")
