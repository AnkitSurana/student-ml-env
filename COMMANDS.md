# 💻 Quick Commands Reference

## Basic

```bash
docker-compose up -d          # Start
docker-compose down           # Stop
docker-compose logs -f        # View logs
docker-compose ps             # Status
```

## Development

```bash
docker-compose exec ml-jupyter bash          # Access shell
docker-compose exec ml-jupyter python script.py  # Run script
docker-compose logs ml-jupyter | grep token  # Get Jupyter token
```

## Troubleshooting

```bash
docker-compose restart              # Restart
docker-compose down -v              # Full reset (deletes data!)
docker system prune -a              # Clean up
docker-compose ps                   # Check status
```

## Vector Databases

```bash
# ChromaDB
curl http://localhost:8000/api/v1/heartbeat

# Qdrant
curl http://localhost:6333/health

# Weaviate
curl http://localhost:8080/v1/.well-known/ready
```

## Databases

```bash
# PostgreSQL
docker-compose exec postgres psql -U postgres

# MongoDB
docker-compose exec mongodb mongosh -u admin -p admin

# Redis
docker-compose exec redis redis-cli -a redis-password
```

See COMMANDS.md for full reference.
