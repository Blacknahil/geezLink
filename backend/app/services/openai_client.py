from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(".env.local")

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
