import aiohttp
import asyncio
import ujson

async def work():
    # blocking call
    value = input("Chat here:\n")
    # did not implement http post due to lax project requirements
    # more details in Report.txt
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8000/random') as resp:
            data = await resp.json()
            # TODO figure a better way to make this deserialization
            print(data["data"][0]["attributes"]["content"])
    print ("ok")

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
