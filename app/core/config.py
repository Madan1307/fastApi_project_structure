from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Iris Prediction API"
    version: str = "1.0.0"
    debug: bool = True
    DATABASE_URL: str
    OPENAI_API_KEY: str | None = None
    GROQ_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()