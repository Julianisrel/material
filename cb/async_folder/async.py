import asyncio

async def main():
    print('Run main:', 'Julian')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(0.5)

    await task
    print('Completed program')

async def foo(text):
     print('Run foo:', text)
     await asyncio.sleep(10)

asyncio.run(main())

