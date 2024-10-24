from pydantic import BaseSettings

class Settings(BaseSettings):
    REPLICATE_API_KEY: str
    REPLICATE_MODEL_NAME: str
    REPLICATE_API_URL: str
    REPLICATE_BASE_URL:str

    class Config:
        env_file = ".env"

settings = Settings()
