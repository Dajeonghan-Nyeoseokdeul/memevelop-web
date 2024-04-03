from abc import ABCMeta, abstractmethod


class HealthService(metaclass=ABCMeta):
    @abstractmethod
    def base_health_check(self) -> bool:
        pass

    @abstractmethod
    def infra_health_check(self) -> bool:
        pass
