from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

def get_settings():
    return Settings()