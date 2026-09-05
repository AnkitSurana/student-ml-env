# Student ML Environment

Cross-platform Docker image for Python, data science, machine learning, and
GenAI development. The public user experience is a single Docker Hub image:
install Docker, run one command, and open the browser IDE. Docker Compose is
kept in this repository for developers who want to build or run the optional
database services.

## Requirements

- Windows: Docker Desktop with the WSL 2 backend
- macOS: Docker Desktop for Apple Silicon or Intel
- Linux: Docker Engine

Verify Docker:

```bash
docker --version
```

## Run from Docker Hub

The image starts code-server automatically. This command works on macOS, Linux,
Git Bash, and WSL:

```bash
mkdir -p projects notebooks data datasets models
docker run -d --name ml-workspace \
  --restart unless-stopped \
  -p 8080:8080 \
  -p 8888:8888 \
  -p 5000:5000 \
  -p 6006:6006 \
  -p 8501:8501 \
  -v "$PWD/projects:/workspace/projects" \
  -v "$PWD/notebooks:/workspace/notebooks" \
  -v "$PWD/data:/workspace/data" \
  -v "$PWD/datasets:/workspace/datasets" \
  -v "$PWD/models:/workspace/models" \
  ankitsurana/student-ml-env:latest
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force projects,notebooks,data,datasets,models
docker run -d --name ml-workspace `
  --restart unless-stopped `
  -p 8080:8080 -p 8888:8888 -p 5000:5000 -p 6006:6006 -p 8501:8501 `
  -v "${PWD}\projects:/workspace/projects" `
  -v "${PWD}\notebooks:/workspace/notebooks" `
  -v "${PWD}\data:/workspace/data" `
  -v "${PWD}\datasets:/workspace/datasets" `
  -v "${PWD}\models:/workspace/models" `
  ankitsurana/student-ml-env:latest
```

Open <http://localhost:8080>. The default `auth none` setting is intended for
localhost-only use. Do not publish this port directly to the internet.

## Optional keys and configuration

No API keys are required to start the image. Pass optional values when the
container is created:

```bash
docker run -d --name ml-workspace \
  --env OPENAI_API_KEY="$OPENAI_API_KEY" \
  --env ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
  -p 8080:8080 -p 8888:8888 -p 5000:5000 -p 6006:6006 -p 8501:8501 \
  -v "$PWD/projects:/workspace/projects" \
  ankitsurana/student-ml-env:latest
```

For several values, create a private `.env` from `.env.example` and use:

```bash
docker run -d --name ml-workspace \
  --env-file .env \
  -p 8080:8080 -p 8888:8888 -p 5000:5000 -p 6006:6006 -p 8501:8501 \
  -v "$PWD/projects:/workspace/projects" \
  ankitsurana/student-ml-env:latest
```

Applications launched inside the container read these variables from
`os.environ`. Values cannot be added to an existing container environment;
recreate the container or use a mounted configuration file.

## Launch tools inside the running container

```bash
docker exec -it ml-workspace ml-env jupyter
docker exec -it ml-workspace ml-env tensorboard
docker exec -it ml-workspace ml-env streamlit /workspace/projects/app.py
docker exec -it ml-workspace ml-env mlflow
docker exec -it ml-workspace ml-env shell
docker exec ml-workspace ml-env python /workspace/projects/example.py
```

JupyterLab, TensorBoard, MLflow, and Streamlit use ports `8888`, `6006`,
`5000`, and `8501`. See `COMMANDS.md` for the complete Docker Hub command
reference.

## Databases and vector stores

The Docker Hub image intentionally does not start sibling database containers.
That keeps `docker run` portable and avoids requiring the container to control
the host Docker daemon. Connect to externally managed services by passing
their host, port, and credentials with `--env` or `--env-file`.

Developers who need the bundled PostgreSQL, MongoDB, Redis, ChromaDB, Qdrant,
Weaviate, Milvus, pgAdmin, and Mongo Express services can use the repository's
Compose environment. It is a development tool, not required by Docker Hub
users:

```bash
git clone https://github.com/AnkitSurana/student-ml-env.git
cd student-ml-env
docker compose up -d
```

Inside that developer environment, service names are `postgres`, `mongodb`,
`redis`, `chromadb`, `qdrant`, `weaviate`, and `milvus`.

## Lifecycle and troubleshooting

```bash
docker ps
docker logs -f ml-workspace
docker stop ml-workspace
docker start ml-workspace
docker rm -f ml-workspace
docker inspect ml-workspace
```

If a port is already in use, change only the host side of the mapping, for
example `-p 18080:8080`. If the image is large or slow, increase Docker
Desktop resources. The full dependency set is architecture- and
resource-sensitive; Docker Desktop must be configured with sufficient RAM and
disk.

## Build and develop

```bash
docker build --tag student-ml-env:local .
docker run --rm -p 8080:8080 student-ml-env:local
```

The repository also contains `docker-compose.yml` for developers, `.env.example`
for configuration documentation, `setup.py`/`setup.sh` for local development,
and `.github/workflows/docker.yml` for CI image builds. See `INSTALL.md` and
`COMMANDS.md` for developer workflows.
