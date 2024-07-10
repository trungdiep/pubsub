import redis
from typing import Any


class EventedRedis:
    def __init__(self, host: str = 'localhost', port: int = 6367,
                 is_sub=False) -> None:
        self.channels = []
        self.redis = redis.Redis(host=host, port=port, decode_responses=True)
        self.pub = self.redis.pubsub()
        self.is_sub = is_sub

    def subcribe(self, channels: list):
        self.channels.extend(channels)
        self.pub.subscribe(*self.channels)

    def handle(self):
        while self.is_sub:
            message = self.pub.get_message()
            if message:
                print(message)

    def publish(self, channel, msg):
        self.redis.publish(channel, msg)

    def unsubscribe(self):
        pub = self.redis.pubsub()
        pub.unsubscribe()
        self.close()

    def close(self):
        self.pub.close()
