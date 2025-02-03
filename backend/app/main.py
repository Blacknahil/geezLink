from fastapi import FastAPI
from app.routes import sessions, chat
from app.services.redis import init_redis, close_redis
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(sessions.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to specific frontend URL (e.g., "http://localhost:3000")
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup():
    await init_redis()

@app.on_event("shutdown")
async def shutdown():
    await close_redis()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
