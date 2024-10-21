import asyncio
import time


async def process_element(el):
    print(f"Processing {el}")
    await asyncio.sleep(5 - el)  # Simulate work with a sleep


async def main():
    tasks = []
    for el in range(10):
        tasks.append(process_element(el))
    await asyncio.gather(*tasks)


temp_time = time.time()
asyncio.run(main())
print(time.time() - temp_time)
