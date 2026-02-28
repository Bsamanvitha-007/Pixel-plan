import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./pixelplan.db")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
UPLOAD_DIR = "uploads"
GENERATED_DIR = "generated"