# rag/vector_store.py

from chromadb import Client
from chromadb.config import Settings

def get_vector_db(persist_directory="rag_db"):
    client = Client(Settings(persist_directory=persist_directory))
    return client.get_or_create_collection(name="mimic-patients")
