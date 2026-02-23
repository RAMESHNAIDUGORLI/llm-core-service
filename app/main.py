from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LLM Core Service")

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "healthy",
            "service": "my first api",
            "version":1.0}