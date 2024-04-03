from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from infra.health.redis.config import RedisConfig
from domain.health.repo.repo import HealthRepo
from domain.health.service.service import HealthService


class HealthContainer(DeclarativeContainer):
    redis_config: RedisConfig
    health_repo: HealthRepo
    health_service: HealthService

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            "infra.health.redis.repo",
        ]
    )

