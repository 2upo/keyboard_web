import asyncio
import json
import logging
import logging.config

import keyboard
from websockets.server import serve

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

ex = {'backtick': '`', 'minus': '-', 'equals': '=', 'left-brace': '[', 'right-brace': ']', 'caps-lock': 'caps lock', 'left-shift': 'left shift', 'right-shift': 'right shift', 'left-ctrl': 'left ctrl', 'left-win': 'left windows', 'left-alt': 'left alt', 'right-alt': 'right alt', 'right-win': 'right windows'}

async def handler(websocket):
    async for message in websocket:
        d = json.loads(message)
        print(d)
        if d.get('message'):
            await websocket.send('pong')
        else:
            key = d['data']['key']
            if key in ex:
                key = ex.get(key)
            try:
                keyboard.press_and_release(key)
            except:
                print(key)


async def main():
    async with serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())


