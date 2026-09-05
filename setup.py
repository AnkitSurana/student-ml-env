#!/usr/bin/env python3
"""Cross-platform setup script for ML/AI Docker environment"""

import platform
import subprocess
import sys
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
    
    def build(self):
        print("\n📦 Building Docker image...\n")
        result = subprocess.run(["docker", "compose", "build"], cwd=self.script_dir)
        if result.returncode == 0:
            print("✅ Build complete\n")
            return True
        print(f"❌ Build failed\n")
        return False
    
    def start(self):
        print("🎬 Starting the ML environment...")
        result = subprocess.run(["docker", "compose", "up", "-d"], cwd=self.script_dir)
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
        print("   • VS Code in browser   http://localhost:8080")
        print("\nAll services share the ml-network network:")
        print("   docker compose ps")
        print("   docker compose exec ml-ide ml-env jupyter")
        print("="*60 + "\n")
    
    def run(self):
        try:
            self.create_directories()
            if not self.check_docker():
                sys.exit(1)
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
