from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from pymongo.server_api import ServerApi
from pymongo import IndexModel
from beanie import init_beanie

from .models import Cart_Items

MONGO_URI = "mongodb://localhost:27017"

client: AsyncIOMotorClient = None
cart_db: AsyncIOMotorDatabase = None
cart_items: AsyncIOMotorCollection = None

doc_models = [Cart_Items]

async def create_db(client: AsyncIOMotorClient):
    global cart_db
    cart_db = client["cart_db"]

async def create_collections(cart_db: AsyncIOMotorDatabase):
    global cart_items
    cart_items = cart_db["cart_items"]

async def check_indexes(cart_items: AsyncIOMotorCollection):
    existing_indexes = cart_items.list_indexes()
    indexes = []
    async for index in existing_indexes:
        indexes.append(index["name"])
    if "product_id_1" not in indexes:
        cart_items.create_index([("product_id", 1)], unique = True)
    #print(indexes)
    

async def connect_to_mongo():
    global client
    try:
        client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi('1'))
        
        await create_db(client=client)
        await create_collections(cart_db=cart_db)
        await check_indexes(cart_items=cart_items)
        
        await init_beanie(database=cart_db, document_models=doc_models)        
        print("Connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e

async def close_connection():
    if client:
        client.close()