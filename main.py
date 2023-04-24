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
        logger.info(d)
        if d.get('data') == 'ping':
            await websocket.send('pong')
        else:
            try:
                key = d['data']['key']
                key = key.lower()
                event = d['data']['event']
                if key in ex:
                    key = ex.get(key)
            except:
                await websocket.send(json.dumps({'errors': 'not valid event type'}))
                logger.error(f'not valid event type: {key}, {event}')
            if event == 0:
                try:
                    keyboard.press_and_release(key)
                except:
                    logger.error(key)
            if event == 1:
                try:
                    keyboard.press(key)
                except:
                    logger.error(key)
            if event == 2:
                try:
                    keyboard.release(key)
                except:
                    logger.error(key)

async def main():
    async with serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())

