from typing import Union, Callable
from asyncio import Future
from websockets.server import serve
import json

Endpoint = Future


class InvalidHandler(Exception):
    """Handler can not process certain request."""


class Handler:
    """WebSocket endpoint implementation."""

    def __init__(self, function: Endpoint, rule: Union[str, int]):
        """
        Create endpoint object from given function and matching rule.

        Args:
            function (Endpoint): maps input message to output msg.
            rule (Union[str, int]): literal which supplies matching of given function resolution.
        """
        self._function = function
        self._rule = rule

    async def check_and_execute(self, msg: dict) -> dict:
        """Check if message satisfies the rule and execute corresponding endpoint.

        Args:
            msg (dict): loaded payload of incoming WS msg.

        Raises:
            InvalidHandler: msg does not satisfy certain rule.

        Returns:
            dict: handler call result.
        """
        if msg["data"] == self._rule and type(msg["data"]) == str:
            return await self._function(msg)
        elif type(msg["data"]) == dict and msg["data"]["event"] == self._rule:
            return await self._function(msg)
        raise InvalidHandler


class WSServer:
    """WebSocket application"""

    def __init__(self):
        """
        Initialize empty array for endpoints
        attach to application with @app.endpoint decorator.
        """
        self._handlers = []

    def endpoint(self, rule: Union[str,
                                   int]) -> Callable[[Endpoint], Endpoint]:
        """Decorator that adds endpoint to handlers pool with corresponding rule

        Args:
            rule (Union[str, int]): literal which supplies matching of given function resolution.

        Returns:
            Callable[[Endpoint], Endpoint]: decorator
        """

        def decorator(function: Endpoint):
            self._handlers.append(Handler(function, rule))
            return function

        return decorator

    async def dispatcher(self, websocket):
        async for message in websocket:
            msg = json.loads(message)
            for handler in self._handlers:
                try:
                    result = await handler.check_and_execute(msg)
                    await websocket.send(json.dumps(result))
                except InvalidHandler as e:
                    continue
            else:
                await websocket.send(
                    json.dumps({'errors': 'not valid event type'}))

    async def start(self, host: str = "127.0.0.1", port: int = 8765):
        """Start listening to websocket events."""
        async with serve(self.dispatcher, host, port):
            await Future()  # run forever
