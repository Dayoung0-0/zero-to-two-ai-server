"""Infrastructure settings placeholder (e.g., env parsing)."""
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PG_HOST: str = os.getenv("PG_HOST")
    PG_PORT: str = os.getenv("PG_PORT")
    PG_USER: str = os.getenv("PG_USER")
    PG_PASSWORD: str = os.getenv("PG_PASSWORD")
    PG_DATABASE: str = os.getenv("PG_DATABASE")

settings = Settings()

# class Settings:
#     def __init__(self):
#         self.env = os.environ.get("APP_ENV", "local")
#
#
# def load_settings() -> Settings:
#     return Settings()
