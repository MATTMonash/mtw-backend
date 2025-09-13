from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_v1_router
from app.config import settings
from app.llms.manager import llm_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events (startup and shutdown)"""
    # Startup
    print(f"[Info] Starting up server in {settings.environment} mode...")

    # Validate and initialise LLMs (importing initialises the LLMs)
    if not llm_manager._models:
        print("[WARN] No LLM models available")
    else:
        print(f"[Success] LLM models available: {list(llm_manager._models.keys())}")

    yield

    # Shutdown
    print("[Info] Shutting down server...")


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
