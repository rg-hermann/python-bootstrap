from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações da aplicação"""

    app_name: str = "Python Bootstrap Service"
    app_version: str = "1.0.0"
    server_port: int = 8080
    debug: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
