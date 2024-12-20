import asyncio
import time
from aiohttp import ClientSession


async def get_weather(city):
    async with ClientSession() as session:
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "APPID": "2a4ff86f9aaa70041ec8e82db64abf56"}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f"In {city} : {weather_json["weather"][0]["main"]}")
            return weather_json["weather"][0]["main"]


async def main(cities_):
    result_dict = dict()
    tasks = list()
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))
        result_dict[city] = None

    results_arr = await asyncio.gather(*tasks)

    result_dict = dict(zip(result_dict.keys(), results_arr))


cities = [
    "Moscow",
    "St. Petersburg",
    "Rostov-on-Don",
    "Kaliningrad",
    "Vladivostok",
    "Minsk",
    "Beijing",
    "Delhi",
    "Istanbul",
    "Tokyo",
    "London",
    "New York",
]

temp_time = time.time()

asyncio.run(main(cities))

print(time.time() - temp_time)
