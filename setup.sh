#!/bin/bash

echo "🚀 Setting up ML/AI Environment..."

# Create directories
mkdir -p notebooks data datasets projects models
mkdir -p chroma_data qdrant_data weaviate_data milvus_data
mkdir -p postgres_data mongodb_data redis_data
echo "✅ Created directories"

# Setup .env
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Edit .env and add your API keys"
    read -p "Press Enter when done..."
fi

# Build
echo "📦 Building Docker image..."
docker-compose build

# Start
echo "🎬 Starting services..."
docker-compose up -d

echo ""
echo "✅ Setup complete!"
echo "📖 Access Jupyter Lab at: http://localhost:8888"
echo "🔑 Get token: docker-compose logs ml-jupyter | grep token"
echo ""
