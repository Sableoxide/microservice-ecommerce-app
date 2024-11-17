from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from beanie import init_beanie
from .models import Cart_Items

MONGO_URI = "mongodb://localhost:27017"

client: AsyncIOMotorClient = None

doc_models = [Cart_Items]

async def connect_to_mongo():
    global client
    try:
        client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi('1'))
        await init_beanie(database=client.cart_db, document_models=doc_models)        
        print("Connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e

async def close_connection():
    if client:
        client.close()