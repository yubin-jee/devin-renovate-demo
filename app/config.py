from pydantic import BaseSettings


class Settings(BaseSettings):
    aws_region: str = "eu-central-1"
    table_name: str = "orders"

    class Config:
        env_prefix = "SVC_ORDERS_"


settings = Settings()
