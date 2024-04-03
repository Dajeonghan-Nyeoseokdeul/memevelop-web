from overrides import override
from dependency_injector.wiring import Provide, inject

from domain.health.repo.repo import HealthRepo
from infra.health.redis.config import RedisConfig
from container.health.container import HealthContainer


class HealthRedis(HealthRepo):
    @inject
    def __init__(
            self,
            config: RedisConfig = Provide[HealthContainer.redis_config]
    ):
        self.config: config

    @override
    def check_health(self) -> bool:
        pass
