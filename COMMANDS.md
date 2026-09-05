# Command reference

The recommended workflow is one Compose project. Docker may create several
containers for the IDE, databases, vector stores, and admin tools, but users
start and stop them as one environment. Every service is attached to the
shared `ml-network`.

## Start and stop everything

```bash
docker compose up -d
docker compose ps
docker compose logs -f ml-ide
docker compose down
```

The default ports are:

| Service | URL or address |
| --- | --- |
| VS Code | http://localhost:8080 |
| JupyterLab | http://localhost:8888 |
| MLflow | http://localhost:5000 |
| TensorBoard | http://localhost:6006 |
| Streamlit apps | http://localhost:8501 |
| ChromaDB | http://localhost:8000 |
| Qdrant | http://localhost:6333 |
| Weaviate | http://localhost:8081 |
| Milvus | localhost:19530 |
| PostgreSQL | localhost:5432 |
| MongoDB | localhost:27017 |
| Redis | localhost:6379 |
| pgAdmin | http://localhost:5050 |
| Mongo Express | http://localhost:8082 |

## Launch applications inside the IDE container

The image includes the `ml-env` launcher:

```bash
docker compose exec ml-ide ml-env help
docker compose exec ml-ide ml-env jupyter
docker compose exec ml-ide ml-env tensorboard
docker compose exec ml-ide ml-env streamlit /workspace/projects/app.py
docker compose exec ml-ide ml-env mlflow
```

These commands stay attached to the terminal. Press `Ctrl-C` to stop the
application without stopping the rest of the environment.

The container also includes Compose control commands. Because the Compose
workflow mounts the Docker socket, these can start sibling services from
inside `ml-ide`. Each command prompts for service settings, saves them to
`/workspace/.env`, starts the service, and validates connectivity:

```bash
docker compose exec -it ml-ide ml-env service postgres
docker compose exec -it ml-ide ml-env service qdrant
docker compose exec -it ml-ide ml-env service redis
```

Choose a service interactively:

```bash
docker compose exec -it ml-ide ml-env services
```

Available individual services are
`postgres`, `mongodb`, `redis`, `chromadb`, `qdrant`, `weaviate`, `milvus`,
`pgadmin`, and `mongo-express`.

In-container service control requires the Compose setup, which mounts the host
Docker socket. The standalone Docker Hub `docker run` command intentionally
does not mount that socket.

Each prompt shows a default. Press Enter to accept it, type a value to
override it, or type `file` to stop and edit `/workspace/.env` in VS Code or
from a shell. Run the same command again after saving. If validation fails,
the command reports the host and port to fix and prints the retry command.

Open a shell or run Python:

```bash
docker compose exec ml-ide ml-env shell
docker compose exec ml-ide ml-env python /workspace/projects/example.py
```

## Service networking

Applications running inside `ml-ide` must use Compose service names, not
`localhost`, to connect to sibling containers:

```bash
export POSTGRES_HOST=postgres
export POSTGRES_PORT=5432
export REDIS_HOST=redis
export QDRANT_HOST=qdrant
export QDRANT_PORT=6333
ml-env python /workspace/projects/example.py
```

Available service hostnames are `postgres`, `mongodb`, `redis`, `chromadb`,
`qdrant`, `weaviate`, and `milvus`.

## Optional keys and parameters

Copy the example only when configuration is needed:

```bash
cp .env.example .env                 # macOS/Linux/Git Bash/WSL
Copy-Item .env.example .env          # Windows PowerShell
docker compose up -d
```

Values in `.env` are passed to the IDE and database containers. Never commit
real credentials.

For a value needed only by one command:

```bash
docker compose exec -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  ml-ide ml-env python /workspace/projects/example.py
```

For values exported inside an interactive container shell:

```bash
docker compose exec -it ml-ide ml-env shell
export OPENAI_API_KEY='your-key'
export MODEL_NAME='your-model'
ml-env python /workspace/projects/example.py
```

Exports apply to processes launched from that shell. They are not persistent
after the container is recreated; use `.env`, `-e`, or `--env-file` when they
must be available on every start.

## Rebuild and inspect

```bash
docker compose build ml-ide
docker compose up -d
docker compose config
docker compose logs -f
docker compose exec ml-ide python --version
docker compose exec ml-ide pip list
```

To remove containers and the shared network:

```bash
docker compose down
```

Do not use `docker compose down --volumes` unless you intentionally want to
delete the database and vector-store named volumes.
