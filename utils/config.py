"""Configuration management"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Central configuration"""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
    
    QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
    WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://weaviate:8080")
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "/workspace/chroma_data")
    
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate_llm_keys(cls):
        """Check which LLM providers are configured"""
        return {
            "openai": bool(cls.OPENAI_API_KEY),
            "anthropic": bool(cls.ANTHROPIC_API_KEY),
            "google": bool(cls.GOOGLE_API_KEY),
        }
