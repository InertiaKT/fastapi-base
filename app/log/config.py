import logging
from typing import Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LogSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="LOG_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    level: Literal["debug", "info", "warn", "warning", "error", "fatal", "critical"] = Field(default="info")

    @property
    def logging_level(self) -> int:
        logging_level_mapping = {
            "debug": logging.DEBUG,
            "info": logging.INFO,
            "warn": logging.WARN,
            "warning": logging.WARNING,
            "error": logging.ERROR,
            "fatal": logging.FATAL,
            "critical": logging.CRITICAL
        }

        if self.level.lower() not in logging_level_mapping.keys():
            raise RuntimeError(f"Log level {self.level} is not supported.")

        return logging_level_mapping[self.level.lower()]