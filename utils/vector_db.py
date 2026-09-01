"""Vector Database utilities"""
import os
from dotenv import load_dotenv

load_dotenv()

class VectorDBConfig:
    """Configuration for vector databases"""
    CHROMA_HOST = os.getenv("CHROMA_HOST", "chromadb")
    CHROMA_PORT = os.getenv("CHROMA_PORT", "8000")
    CHROMA_URL = f"http://{CHROMA_HOST}:{CHROMA_PORT}"
    
    QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant")
    QDRANT_PORT = os.getenv("QDRANT_PORT", "6333")
    QDRANT_URL = f"http://{QDRANT_HOST}:{QDRANT_PORT}"
    
    WEAVIATE_HOST = os.getenv("WEAVIATE_HOST", "weaviate")
    WEAVIATE_PORT = os.getenv("WEAVIATE_PORT", "8080")
    WEAVIATE_URL = f"http://{WEAVIATE_HOST}:{WEAVIATE_PORT}"
    
    MILVUS_HOST = os.getenv("MILVUS_HOST", "milvus")
    MILVUS_PORT = int(os.getenv("MILVUS_PORT", "19530"))

class VectorDBManager:
    """Unified vector database interface"""
    
    @staticmethod
    def check_all_connections():
        """Check all vector database connections"""
        print("\n" + "="*50)
        print("VECTOR DATABASE CONNECTION CHECK")
        print("="*50 + "\n")
        
        results = {}
        
        # ChromaDB
        try:
            import chromadb
            chromadb.HttpClient(
                host=VectorDBConfig.CHROMA_HOST,
                port=int(VectorDBConfig.CHROMA_PORT)
            )
            results["ChromaDB"] = True
            print("✅ ChromaDB (Local, Simple)")
        except Exception as e:
            results["ChromaDB"] = False
            print(f"❌ ChromaDB: {str(e)[:40]}")
        
        # Qdrant
        try:
            from qdrant_client import QdrantClient
            QdrantClient(
                host=VectorDBConfig.QDRANT_HOST,
                port=int(VectorDBConfig.QDRANT_PORT)
            )
            results["Qdrant"] = True
            print("✅ Qdrant (Production-ready)")
        except Exception as e:
            results["Qdrant"] = False
            print(f"❌ Qdrant: {str(e)[:40]}")
        
        # Weaviate
        try:
            import weaviate
            weaviate.Client(
                url=VectorDBConfig.WEAVIATE_URL,
                timeout_config=(5, 15)
            )
            results["Weaviate"] = True
            print("✅ Weaviate (Enterprise)")
        except Exception as e:
            results["Weaviate"] = False
            print(f"❌ Weaviate: {str(e)[:40]}")
        
        # Milvus
        try:
            from pymilvus import connections
            connections.connect(
                "default",
                host=VectorDBConfig.MILVUS_HOST,
                port=VectorDBConfig.MILVUS_PORT
            )
            results["Milvus"] = True
            print("✅ Milvus (Scalable)")
        except Exception as e:
            results["Milvus"] = False
            print(f"❌ Milvus: {str(e)[:40]}")
        
        print("\n" + "="*50 + "\n")
        return results
