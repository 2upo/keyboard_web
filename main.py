import asyncio
import logging
import logging.config
from wsserver import WSServer
import keyboard

logging.config.fileConfig(fname="file.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

keys = "backtick,1,2,3,4,5,6,7,8,9,0,minus,equals,backspace,tab,q,w,e,r,t,y,u,i,o,p,left-brace,right-brace,backslash,caps-lock,a,s,d,f,g,h,j,k,l,semicolon,apostrophe,enter,left-shift,z,x,c,v,b,n,m,comma,period,slash,right-shift,left-ctrl,left-win,left-alt,spacebar,right-alt,right-win,num-divide,num-multiply,num-subtract,num-7,num-8,num-9,num-add,num-4,num-5,num-6,num-1,num-2,num-3,num-enter,num-0,num-decimal"
keys_mapping = {
    "backtick": "`",
    "minus": "-",
    "equals": "=",
    "left-brace": "[",
    "right-brace": "]",
    "caps-lock": "caps lock",
    "left-shift": "left shift",
    "right-shift": "right shift",
    "left-ctrl": "left ctrl",
    "left-win": "left windows",
    "left-alt": "left alt",
    "right-alt": "right alt",
    "right-win": "right windows",
}

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

app = WSServer()


@app.endpoint('ping')
async def ping(msg: dict):
    return {'data': 'pong', 'errors': None}


@app.endpoint(0)
async def press_and_release(msg: dict):
    key = msg['data']['key']
    key = key.lower()
    if key in keys_mapping:
        key = keys_mapping.get(key)

    try:
        keyboard.press_and_release(key)
    except:
        logger.error(key)


@app.endpoint(1)
async def press(msg: dict):
    key = msg['data']['key']
    key = key.lower()
    if key in keys_mapping:
        key = keys_mapping.get(key)

    try:
        keyboard.press(key)
    except:
        logger.error(key)


@app.endpoint(2)
async def release(msg: dict):
    key = msg['data']['key']
    key = key.lower()
    if key in keys_mapping:
        key = keys_mapping.get(key)

    try:
        keyboard.release(key)
    except:
        logger.error(key)


asyncio.run(app.start("0.0.0.0", 8765))
