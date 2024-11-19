from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from .routes import cart_service
from .database import connect_to_mongo, close_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await connect_to_mongo()
        
        print("Connected to the DB successfully")
    except Exception as e:
        print(f"Connection to DB FAILED: {e}")
        raise e
    yield
    await close_connection()
    
DESCRIPTION = """
    This is a microservice.
"""

app = FastAPI(
    title = "CART MICROSERVICE",
    description = DESCRIPTION,
    version = "1.0.0",
    contact = {
        "name": "Goko Frank",
        "email": "frank432kinuthia@gmail.com",
    },
    license_info = {
        "name": "MIT",
        "url": "https://github.com/Sableoxide/microservice-ecommerce-app/blob/main/LICENSE",
    },
    lifespan = lifespan
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def internal_server_error_handler(request: Request, exc: Exception):
    # Log the error silently (optional)
    # log.error(f"Internal Server Error: {exc}") 
    
    # Return a custom JSON response
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "An unexpected error occurred. Please try again later."}
    )



@app.get("/")
async def read_route():
    
    return {"msg": "welcome"}

app.include_router(cart_service)

# uvicorn cart_service.main:app --reload
