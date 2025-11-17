import os
from urllib.parse import urlparse

import pymssql
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_pcs_db():
    parsed = urlparse(os.getenv('PCS_DB_URL'))
    return pymssql.connect(
        server=parsed.hostname,
        user=parsed.username,
        password=parsed.password,
        database=parsed.path.lstrip('/'),
        tds_version='7.3'
    )


@app.get("/")
async def root():
    routes = []
    # Exclude auto-generated documentation endpoints
    excluded_paths = {"/openapi.json", "/docs", "/redoc"}
    excluded_prefixes = ["/docs/"]
    
    for route in app.routes:
        if hasattr(route, "path") and hasattr(route, "methods"):
            path = route.path
            # Skip excluded paths and paths starting with excluded prefixes
            if path not in excluded_paths and not any(path.startswith(prefix) for prefix in excluded_prefixes):
                routes.append({
                    "path": path,
                    "methods": list(route.methods)
                })
    return {"routes": routes}


@app.get("/health")
async def health():
    return {"status": "healthy"}

