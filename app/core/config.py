from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]  # trỏ về folder chứa app/

class Settings(BaseSettings):
    # SQLite file nằm ngay cạnh app/ (root project)
    DATABASE_URL: str = f"sqlite:///{(BASE_DIR / 'dev.db').as_posix()}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
