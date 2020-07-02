import asyncio
import websockets
import pathlib
import ssl
import time

async def hello():
    
    async with websockets.connect('wss://echo.websocket.org/') as websocket:
        
        # name = input("What's your name? ")
        name = "onedi"
        a = time.time()
        await websocket.send(name)
        # print(f"> {name}")

        greeting = await websocket.recv()
        print((time.time() - a) *1000, "22") 
        print(f"< {greeting}")
        greeting = await websocket.recv()

s = time.time()
asyncio.get_event_loop().run_until_complete(hello())  
print((time.time() - s) *1000) 





