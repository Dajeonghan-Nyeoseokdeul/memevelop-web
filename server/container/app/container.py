import argparse
import tomlkit
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton

from util.app.app import MiddlewareConfig, RunConfig
from util.app.arg_parser import parse_args
from controller.constructor import ApiConstructor


class AppInitializeContainer(DeclarativeContainer):
    with open("core/app/config.toml", "r") as config_file:
        toml_config: dict = tomlkit.load(config_file)

    middleware_config: MiddlewareConfig = Singleton(
        MiddlewareConfig,
        **toml_config[parse_args.runtime]["middleware"]
    )

    run_config: RunConfig = Singleton(
        RunConfig,
        **toml_config[parse_args.runtime]["run"]
    )

    api_routers: ApiConstructor = Singleton(
        ApiConstructor
    )

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            "util.app.constructor",
        ]
    )
