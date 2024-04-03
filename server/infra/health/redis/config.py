from pydantic import BaseModel


class RedisConfig(BaseModel):
    url: str
    user: str
    password: str
    port: int
