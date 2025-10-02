import asyncio


async def never_awaited(num: int):
    while True:
        print(f'never awaited: {num}')
        await asyncio.sleep(0)  # without this never callback to even loop


async def main():
    tasks = []
    for idx in range(5):
        task = asyncio.create_task(never_awaited(idx))
        tasks.append(task)
    # await asyncio.gather(*tasks)  # without this we do not await never_awaited
    print('main completed')


if __name__ == '__main__':
    asyncio.run(main())
