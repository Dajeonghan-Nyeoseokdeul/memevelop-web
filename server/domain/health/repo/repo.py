from abc import ABCMeta, abstractmethod


class HealthRepo(metaclass=ABCMeta):
    @abstractmethod
    def check_health(self) -> bool:
        pass
