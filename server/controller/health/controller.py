from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from domain.health.service.service import HealthService
from container.health.container import HealthContainer


health_router: APIRouter = APIRouter()


@health_router.get('/health')
@inject
async def base_health_check(
        service: HealthService = Depends(Provide[HealthContainer.health_service])
):
    return None

