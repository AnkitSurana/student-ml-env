# Student ML Environment

A portable Docker machine-learning environment for Windows, macOS, and Linux.
It provides browser-based VS Code, JupyterLab, the Python ML stack, local
databases, vector databases, and admin tools.

## How the environment works

Use **Docker Compose** as the normal entry point. One Compose command starts
the complete environment. Docker creates separate containers internally
because databases and admin tools are maintained as separate services, but
users operate them as one project:

```text
Compose project
├── ml-ide       VS Code, Python, JupyterLab, MLflow, TensorBoard, Streamlit
├── databases    PostgreSQL, MongoDB, Redis
├── vector stores ChromaDB, Qdrant, Weaviate, Milvus
└── admin tools  pgAdmin, Mongo Express
```

All services share the `ml-network` network. From the IDE container, use
service names such as `postgres` or `qdrant`; do not use `localhost` for
sibling containers.

## Requirements

- Windows 10/11: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  with the WSL 2 backend.
- macOS: Docker Desktop for Apple Silicon or Intel.
- Linux: Docker Engine and the Docker Compose plugin.

Verify the installation:

```bash
docker --version
docker compose version
```

## Recommended installation

Clone the repository and start the complete environment:

```bash
git clone https://github.com/AnkitSurana/student-ml-env.git
cd student-ml-env
docker compose up -d
```

Open VS Code at <http://localhost:8080>. Check all containers:

```bash
docker compose ps
docker compose logs -f ml-ide
```

Stop the complete environment:

```bash
docker compose down
```

See `COMMANDS.md` for the full command list and service URLs.

## Launch applications inside Docker

The `ml-ide` container starts code-server automatically. Other applications
are launched directly from the same container with `ml-env`:

```bash
docker compose exec ml-ide ml-env jupyter
docker compose exec ml-ide ml-env tensorboard
docker compose exec ml-ide ml-env streamlit /workspace/projects/app.py
docker compose exec ml-ide ml-env mlflow
```

You can also start one Compose service at a time from inside the IDE
container. The command prompts for that service's host, port, credentials, and
other settings, saves them to `/workspace/.env`, starts the service, and
validates connectivity:

```bash
docker compose exec -it ml-ide ml-env service postgres
docker compose exec -it ml-ide ml-env service qdrant
docker compose exec -it ml-ide ml-env service redis
```

Or choose a service interactively:

```bash
docker compose exec -it ml-ide ml-env services
```

Supported services include `postgres`, `mongodb`,
`redis`, `chromadb`, `qdrant`, `weaviate`, `milvus`, `pgadmin`, and
`mongo-express`.

These in-container service controls are available in the Compose image because
it mounts `/var/run/docker.sock`. A standalone Docker Hub `docker run` does
not mount that socket, so use Compose when you want `ml-env service` to start
sibling containers.

Each prompt shows a default. Press Enter to accept it, type a value to
override it, or type `file` to edit `/workspace/.env` in VS Code or a shell.
Run the same command again after saving. If the service starts but validation
fails, the command reports the unreachable host or port and gives the retry
command.

Open JupyterLab at <http://localhost:8888>, TensorBoard at
<http://localhost:6006>, Streamlit at <http://localhost:8501>, and MLflow at
<http://localhost:5000>. All application ports are already published by
Compose.

Run a shell or Python script:

```bash
docker compose exec -it ml-ide ml-env shell
docker compose exec ml-ide ml-env python /workspace/projects/example.py
```

## Connect to databases

The database and vector services are already on the same Docker network:

```bash
docker compose exec -it ml-ide ml-env shell
export POSTGRES_HOST=postgres
export POSTGRES_PORT=5432
export QDRANT_HOST=qdrant
export QDRANT_PORT=6333
ml-env python /workspace/projects/example.py
```

Available internal hostnames are `postgres`, `mongodb`, `redis`, `chromadb`,
`qdrant`, `weaviate`, and `milvus`. Host applications can use the published `localhost` ports listed in
`COMMANDS.md`. Database data is stored in Docker-managed named volumes so
services started from inside the container and services started from the host
use the same persistent data.

## Optional keys and environment variables

No API keys are required to start the environment. To configure integrations,
copy the example file and edit the copy:

```bash
cp .env.example .env                 # macOS/Linux/Git Bash/WSL
Copy-Item .env.example .env          # Windows PowerShell
docker compose up -d
```

The `.env` file is ignored by Git. You can also export values from an
interactive shell inside `ml-ide`:

```bash
docker compose exec -it ml-ide ml-env shell
export OPENAI_API_KEY='your-key'
export MODEL_NAME='your-model'
ml-env python /workspace/projects/example.py
```

Those exports are inherited by applications launched from that shell. Use
`.env` when a value must be supplied every time the container starts.

## Docker Hub image

The Docker Hub image is useful when you only need the IDE and Python
environment:

```bash
docker run -d --name ml-workspace \
  -p 8080:8080 \
  -v "$PWD/projects:/workspace/projects" \
  ankitsurana/student-ml-env:latest
```

This standalone command does **not** start sibling databases. Use the Compose
workflow above for the complete, networked environment.

## Local build

Use the cross-platform helper:

```bash
python3 setup.py       # macOS/Linux
python setup.py        # Windows
```

Or on macOS/Linux, Git Bash, or WSL:

```bash
bash setup.sh
```

Manual build:

```bash
docker compose build ml-ide
docker compose up -d
```

Do not expose code-server publicly without authentication and TLS. The
default no-token mode is intended for localhost-only development.
