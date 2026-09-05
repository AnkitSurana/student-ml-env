#!/bin/bash

echo "🚀 Setting up ML/AI Environment..."

# Create directories
mkdir -p notebooks data datasets projects models
mkdir -p chroma_data qdrant_data weaviate_data milvus_data
mkdir -p postgres_data mongodb_data redis_data
echo "✅ Created directories"

# Build
echo "📦 Building Docker image..."
docker compose build

# Start the single Compose environment
echo "🎬 Starting the ML environment..."
docker compose up -d

echo ""
echo "✅ Setup complete!"
echo "📖 Open VS Code at: http://localhost:8080"
echo "📖 Start Jupyter: docker compose exec ml-ide ml-env jupyter"
echo "📖 Check services: docker compose ps"
echo ""
