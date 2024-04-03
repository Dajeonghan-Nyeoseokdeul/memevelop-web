from overrides import override
from dependency_injector.wiring import inject, Provide

from domain.health.service.service import HealthService
from domain.health.repo.repo import HealthRepo
from container.health.container import HealthContainer


class HealthApplication(HealthService):
    @inject
    def __init__(
            self,
            repo: HealthRepo = Provide[HealthContainer.health_repo]
    ):
        self.repo: HealthRepo = repo

    @override
    def base_health_check(self) -> bool:
        pass

    @override
    def infra_health_check(self) -> bool:
        pass







