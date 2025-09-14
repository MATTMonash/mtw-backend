from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_v1_router
from app.config import settings
from app.llms.manager import llm_manager
from app.logging import get_logger, setup_logging

setup_logging(level=settings.log_level)
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events (startup and shutdown)"""
    # Startup
    logger.info(f"Starting up server in {settings.environment} mode...")

    # Validate and initialise LLMs (importing initialises the LLMs)
    if not llm_manager._models:
        logger.warning("No LLM models available")
    else:
        logger.info(f"LLM models available: {list(llm_manager._models.keys())}")

    yield

    # Shutdown
    logger.info("Shutting down server...")


app = FastAPI(
    title="More Than Words Server",
    description="More Than Words Agentic AI FastAPI Server",
    version="0.0.1",
    docs_url="/",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix="/api/v1")
