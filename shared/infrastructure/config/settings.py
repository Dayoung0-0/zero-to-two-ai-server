"""Infrastructure settings placeholder (e.g., env parsing)."""
import os


class Settings:
    def __init__(self):
        self.env = os.environ.get("APP_ENV", "local")

        # Database 설정
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", "5432")
        db_name = os.getenv("DB_DATABASE", "postgres")
        db_user = os.getenv("DB_USERNAME", "postgres")
        db_pass = os.getenv("DB_PASSWORD", "")

        self.DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


def load_settings() -> Settings:
    return Settings()
