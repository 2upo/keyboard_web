from websockets.sync.client import connect
import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send(input())
        message = websocket.recv()
        logger.info(message)

hello()