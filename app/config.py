from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SVC_ORDERS_")

    aws_region: str = "eu-central-1"
    table_name: str = "orders"


settings = Settings()
