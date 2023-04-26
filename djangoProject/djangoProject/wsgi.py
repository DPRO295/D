import asyncio
from channels.consumer import AsyncConsumer

class MyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })

        while True:
            message = await self.receive()
            if message is None:
                break

            await self.send({
                "type": "websocket.send",
                "text": message["text"]
            })

async def application(scope, receive, send):
    if scope["type"] == "http":
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        })
        await send({
            "type": "http.response.body",
            "body": b"Hello, world!",
        })
    elif scope["type"] == "websocket":
        consumer = MyConsumer()
        await consumer.websocket_connect({
            "type": "websocket.connect",
            "path": scope["path"],
            "query_string": scope["query_string"],
            "headers": scope["headers"],
        })
        await asyncio.gather(
            consumer.run(),
            send({
                "type": "websocket.close"
            }),
        )