from pydantic import BaseSettings

class AppSettings(BaseSettings):
    DEBUG: str
    APP_TITLE: str
    VERSION: str
    SECRET_KEY: str

    class Config:
        case_sensitive = True
        env_file = 'app/.env'

settings = AppSettings()