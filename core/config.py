from pydantic_settings import BaseSettings

class Config(BaseSettings):
    
    MYSQL_URL: str
    
    class Config:
        env_file = ".env"

config = Config()
