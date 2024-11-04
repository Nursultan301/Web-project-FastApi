from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key_prefix: str = "/api/v1"
    db_url: str = (
        "postgresql+asyncpg://shop_user:310198iko@172.28.4.106:5445/db_shop_test"
    )
    db_echo: bool = True


settings = Settings()
