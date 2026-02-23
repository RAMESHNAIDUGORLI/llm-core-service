from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LLM Core Service"
    environment: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()