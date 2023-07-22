import asyncio
import datetime

import requests

import tournois

part1 = {}
part2 = {}
part3 = {}
part4 = {}


async def get_tournois(client, forced=False):
    global part1, part2, part3, part4
    a = requests.get(
        "https://op-core.pokemon.com/api/v2/event_locator/search/?latitude=49.2869081268061&longitude=3.848719678847761&distance=200")
    json_data = a.json()
    part1 = json_data
    a = requests.get(
        "https://op-core.pokemon.com/api/v2/event_locator/search/?latitude=45.7812786064092&longitude=6.802280022386639&distance=200")
    json_data = a.json()
    part2 = json_data
    a = requests.get(
        "https://op-core.pokemon.com/api/v2/event_locator/search/?latitude=44.78039749019867&longitude=1.5082195032643173&distance=200")
    json_data = a.json()
    part3 = json_data
    a = requests.get(
        "https://op-core.pokemon.com/api/v2/event_locator/search/?latitude=47.12493383322305&longitude=-1.395448039079782&distance=200")
    json_data = a.json()
    part4 = json_data
    tournois.tournois = []
    for i in part1["activities"]:
        if "category" in i["metadata"]:
            if i["metadata"]["category"] == "vg_mod":
                if not [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                        i["address"]["location_map_link"], i["name"], i["when"]] in tournois.tournois:
                    tournois.tournois.append(
                        [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                         i["address"]["location_map_link"], i["name"], i["when"]])
    for i in part2["activities"]:
        if "category" in i["metadata"]:
            if i["metadata"]["category"] == "vg_mod":
                if not [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                        i["address"]["location_map_link"], i["name"], i["when"]] in tournois.tournois:
                    tournois.tournois.append(
                        [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                         i["address"]["location_map_link"], i["name"], i["when"]])
    for i in part3["activities"]:
        if "category" in i["metadata"]:
            if i["metadata"]["category"] == "vg_mod":
                if not [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                        i["address"]["location_map_link"], i["name"], i["when"]] in tournois.tournois:
                    tournois.tournois.append(
                        [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                         i["address"]["location_map_link"], i["name"], i["when"]])
    for i in part4["activities"]:
        if "category" in i["metadata"]:
            if i["metadata"]["category"] == "vg_mod":
                if not [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                        i["address"]["location_map_link"], i["name"], i["when"]] in tournois.tournois:
                    tournois.tournois.append(
                        [i["address"]["city"], i["address"]["postal_code"], i["address"]["country"],
                         i["address"]["location_map_link"], i["name"], i["when"]])
    await tournois.filter_tournois()
    await tournois.send_message(client)
    if not forced:
        await init_routine(client)


async def init_routine(client):
    now = datetime.datetime.now()
    if now.hour >= 8:
        date = datetime.datetime(now.year, now.month, now.day + 1, hour=8)
    else:
        date = datetime.datetime(now.year, now.month, now.day, hour=8)
    to_wait = date.timestamp() - datetime.datetime.now().timestamp()  # Time to wait
    await asyncio.sleep(to_wait)
    await get_tournois(client)
