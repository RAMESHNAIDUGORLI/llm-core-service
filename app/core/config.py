from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LLM Core Service"
    environment: str = "dev"
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()