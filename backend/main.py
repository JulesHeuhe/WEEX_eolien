from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .analysis_registry import ANALYSIS_HANDLERS, run_analysis


app = FastAPI(title="WEEX Eolien API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/analyses")
def list_analyses() -> dict[str, list[str]]:
    return {"analyses": sorted(ANALYSIS_HANDLERS.keys())}


@app.get("/api/analyse/{analysis_id}")
def analyse_by_id(analysis_id: str) -> dict[str, Any]:
    return run_analysis(analysis_id)


@app.get("/api/analyse/main-louis")
def analyse_main_louis() -> dict[str, Any]:
    # Legacy endpoint kept for frontend compatibility.
    return run_analysis("main-louis")
