from fastapi import FastAPI

from app.routes.player_routes import router as player_router
from app.routes.auth_routes import router as auth_router


app = FastAPI(
    title="Tic-Tac-Toe API",
    version="1.0.0"
)


app.include_router(player_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Tic-Tac-Toe Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "database": "CONNECTED"
    }