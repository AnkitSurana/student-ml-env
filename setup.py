#!/usr/bin/env python3
"""Cross-platform setup script for ML/AI Docker environment"""

import os, sys, shutil, subprocess, platform
from pathlib import Path

class Setup:
    def __init__(self):
        self.os_type = platform.system()
        self.script_dir = Path(__file__).parent
        print(f"\n{'='*50}\nML/AI Environment Setup\nOS: {self.os_type}\n{'='*50}\n")
    
    def create_directories(self):
        print("📁 Creating directories...")
        for dir_name in ['notebooks', 'data', 'datasets', 'projects', 'models', 
                         'chroma_data', 'qdrant_data', 'weaviate_data', 'milvus_data',
                         'postgres_data', 'mongodb_data', 'redis_data', 'utils']:
            (self.script_dir / dir_name).mkdir(exist_ok=True)
            print(f"   ✓ {dir_name}")
        print("✅ Done\n")
    
    def check_docker(self):
        print("🐳 Checking Docker...")
        try:
            result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"   ✓ {result.stdout.strip()}\n")
                return True
        except FileNotFoundError:
            pass
        print("❌ Docker not found!")
        print("   Download: https://www.docker.com/products/docker-desktop\n")
        return False
    
    def setup_env(self):
        print("⚙️  Setting up .env...")
        env_path = self.script_dir / ".env"
        if not env_path.exists():
            shutil.copy(self.script_dir / ".env.example", env_path)
            print("   ✓ Created from template")
        print("   ⚠️  Edit .env and add your API keys")
        print("   Command: nano .env (Mac/Linux) or notepad .env (Windows)\n")
        input("   Press Enter when done...")
    
    def build(self):
        print("\n📦 Building Docker image...\n")
        result = subprocess.run(["docker-compose", "build"], cwd=self.script_dir, 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Build complete\n")
            return True
        print(f"❌ Build failed\n")
        return False
    
    def start(self):
        print("🎬 Starting services...")
        result = subprocess.run(["docker-compose", "up", "-d"], cwd=self.script_dir,
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Services started\n")
            return True
        print(f"❌ Failed to start\n")
        return False
    
    def print_info(self):
        print("="*60)
        print("✅ SETUP COMPLETE!")
        print("="*60)
        print("\n📖 Services:\n")
        services = {
            "Jupyter Lab": "http://localhost:8888",
            "ChromaDB": "http://localhost:8000",
            "Qdrant": "http://localhost:6333",
            "Weaviate": "http://localhost:8080",
            "pgAdmin": "http://localhost:5050",
        }
        for name, url in services.items():
            print(f"   • {name:20} {url}")
        print(f"\n📖 Get Jupyter token:\n   docker-compose logs ml-jupyter | grep token\n")
        print("="*60 + "\n")
    
    def run(self):
        try:
            self.create_directories()
            if not self.check_docker():
                sys.exit(1)
            self.setup_env()
            if not self.build():
                sys.exit(1)
            if not self.start():
                sys.exit(1)
            self.print_info()
        except KeyboardInterrupt:
            print("\n\n❌ Cancelled\n")
            sys.exit(1)

if __name__ == "__main__":
    Setup().run()
