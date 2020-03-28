import aiohttp
import asyncio
import ujson

# endpoint should be as string, post_process a function
async def getJson(api_endpoint, post_process):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_endpoint) as resp:
            data = await resp.json()
            return post_process(data)


async def work():
    while (True):
        # blocking call
        value = input("Chat here:\n")
        await getJson('http://localhost:8000/random', lambda x : print (x["data"][0]["attributes"]["content"]))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(work())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
