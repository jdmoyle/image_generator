from fastapi import FastAPI
from app.routers import image
from app.utils.logging import setup_logger

# Initialize FastAPI app
app = FastAPI(
    title="Replicate Image Generation API",
    description="API to interact with Replicate's Image Generation endpoint",
    version="1.0.0",
)

# Setup logger
logger = setup_logger("ReplicateAPI")

# Include the routers
app.include_router(image.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the FastAPI application...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the FastAPI application...")
