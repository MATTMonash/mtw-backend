from enum import Enum
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Settings(BaseSettings):
    environment: Environment = Environment.DEVELOPMENT

    google_api_key: str | None = None

    cors_origins: list[str] = ["*"]

    ollama_api_url: str = "http://localhost:11434/api/tags"

    # Logging configuration
    log_level: LogLevel = LogLevel.INFO

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    s = Settings()

    return s


settings = get_settings()
