import asyncio
import datetime

import requests

import pokequizz
import tournois

positions = [[49.2869081268061, 3.848719678847761], [45.7812786064092, 6.802280022386639],
             [44.78039749019867, 1.5082195032643173], [47.12493383322305, -1.395448039079782]]
results = []


async def get_tournois(client, forced=False):
    global results
    results = []
    for p in positions:
        a = requests.get(
            f"https://op-core.pokemon.com/api/v2/event_locator/search/?latitude={p[0]}&longitude={p[1]}&distance=200")
        json_data = a.json()
        results.append(json_data)

    tournois.tournois = []
    for i in results:
        result = i["activities"]
        for r in result:
            if "category" in r["metadata"]:
                if r["metadata"]["category"] == "vg_mod":
                    if not [r["address"]["city"], r["address"]["postal_code"], r["address"]["country"],
                            r["address"]["location_map_link"], r["name"], r["when"]] in tournois.tournois:
                        tournois.tournois.append(
                            [r["address"]["city"], r["address"]["postal_code"], r["address"]["country"],
                             r["address"]["location_map_link"], r["name"], r["when"]])
    await tournois.filter_tournois()
    await tournois.send_message(client)
    if not forced:
        await init_routine(client)


async def init_routine(client):
    now = datetime.datetime.now()
    if now.hour >= 8:
        tomorrow = now + datetime.timedelta(1)
        date = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, hour=8)
    else:
        date = datetime.datetime(now.year, now.month, now.day, hour=8)
    to_wait = date.timestamp() - datetime.datetime.now().timestamp()  # Time to wait
    await asyncio.sleep(to_wait)
    pokequizz.init_poke()
    await get_tournois(client)
