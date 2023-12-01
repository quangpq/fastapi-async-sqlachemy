from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_STR: str = "/api"
    DEBUGGING: bool = False

    DB_USER: str = "admin"
    DB_PASSWORD: str = "12345678"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_NAME: str = "demo"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()
