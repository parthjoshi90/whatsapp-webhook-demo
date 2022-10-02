from pydantic import BaseSettings

class AppSettings(BaseSettings):
    DEBUG: str
    APP_TITLE: str
    VERSION: str
    DATABASE_URI: str
    DATABASE_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str

    class Config:
        case_sensitive = True
        env_file = '.env'

settings = AppSettings()