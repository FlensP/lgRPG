async def run(ctx, proposition, client):
    chan = client.get_channel(1124767717463961681)
    await chan.send(f"Proposition de {ctx.user.name} : {proposition}")
    await ctx.response.send_message("La proposition a été soumise. Attention, les abus seront sanctionnés")
