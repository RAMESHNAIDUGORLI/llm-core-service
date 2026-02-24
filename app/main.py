from fastapi import FastAPI
from app.routers import chat
from app.routers import health
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LLM Core Service")
app.include_router(health.router)
logger.info("Testing chat router now")
app.include_router(chat.router)
