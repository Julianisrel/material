import asyncio



async def fetch_data():
    print('Fetch data')
    await asyncio.sleep(2)
    print('Fetching Done')
    return { 'json_data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())


    value = await task1
    print(value)
    await task2

asyncio.run(main())