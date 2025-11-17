from fastapi import FastAPI

app = FastAPI()


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

