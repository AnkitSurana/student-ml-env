# Student ML Environment

A portable Docker ML workspace with the Python packages, browser-based VS
Code, JupyterLab, and optional local databases already installed. It works on
Windows, macOS, and Linux wherever Docker Desktop or Docker Engine is
available.

## Requirements

Install Docker Desktop on Windows/macOS, or Docker Engine plus the Compose
plugin on Linux:

- Windows 10/11: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  with the WSL 2 backend.
- macOS: Docker Desktop for Apple Silicon or Intel.
- Linux: Docker Engine and `docker compose`.

Check the installation:

```text
docker --version
docker compose version
```

## Fastest start: Docker Hub

Create directories for files that should survive container replacement, then
start the image. The commands below use POSIX shell syntax (macOS/Linux,
Git Bash, or WSL):

```bash
mkdir -p projects notebooks data datasets models
docker run -d --name ml-workspace \
  -p 8080:8080 \
  -p 8888:8888 \
  -v "$PWD/projects:/workspace/projects" \
  -v "$PWD/notebooks:/workspace/notebooks" \
  -v "$PWD/data:/workspace/data" \
  -v "$PWD/datasets:/workspace/datasets" \
  -v "$PWD/models:/workspace/models" \
  ankitsurana/student-ml-env:latest
```

Windows PowerShell equivalent:

```powershell
New-Item -ItemType Directory -Force projects,notebooks,data,datasets,models
docker run -d --name ml-workspace `
  -p 8080:8080 `
  -p 8888:8888 `
  -v "${PWD}\projects:/workspace/projects" `
  -v "${PWD}\notebooks:/workspace/notebooks" `
  -v "${PWD}\data:/workspace/data" `
  -v "${PWD}\datasets:/workspace/datasets" `
  -v "${PWD}\models:/workspace/models" `
  ankitsurana/student-ml-env:latest
```

Open **VS Code** at <http://localhost:8080>. The default image starts
code-server automatically and does not require an API key or login token when
you publish it to localhost.

## Start services when needed

The main container stays focused on the IDE. Start JupyterLab on demand:

```bash
docker exec -it ml-workspace ml-env jupyter
```

Then open <http://localhost:8888>. Open a shell or run a script:

```bash
docker exec -it ml-workspace ml-env shell
docker exec ml-workspace ml-env python /workspace/projects/example.py
```

The standalone Docker Hub image contains database clients, but database
servers are separate containers. Use the Compose setup below when you need
local PostgreSQL, MongoDB, Redis, or vector databases.

## Compose setup with optional databases

Clone the repository, then run the IDE:

```bash
git clone https://github.com/AnkitSurana/student-ml-env.git
cd student-ml-env
docker compose up -d ml-ide
```

Start service groups only when required:

```bash
docker compose --profile database up -d  # PostgreSQL, MongoDB, Redis
docker compose --profile vector up -d    # ChromaDB, Qdrant, Weaviate, Milvus
docker compose --profile admin up -d     # pgAdmin and Mongo Express
```

Start one service:

```bash
docker compose --profile database up -d postgres
docker compose --profile vector up -d qdrant
```

From the IDE container, use these service names as hostnames:
`postgres`, `mongodb`, `redis`, `chromadb`, `qdrant`, `weaviate`, and `milvus`.

Stop the environment:

```bash
docker compose down
# Add --volumes only when you intentionally want to delete named volumes.
```

## API keys and runtime configuration

API keys are optional. Do not put secrets in the Dockerfile or commit them to
Git. Supply a key when creating the container:

```bash
docker run -d --name ml-workspace \
  -p 8080:8080 \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  ankitsurana/student-ml-env:latest
```

For multiple values, create a private file from `.env.example` and pass it at
creation time:

```bash
docker run -d --name ml-workspace \
  -p 8080:8080 \
  --env-file .env \
  ankitsurana/student-ml-env:latest
```

With Compose, copy `.env.example` to `.env` in the repository directory and
run `docker compose up -d ml-ide`. The `.env` file is ignored by Git and is
not required for the default setup.

### Can I add configuration after `docker run`?

Yes, but the method matters:

1. **Environment variables:** Docker does not add new container environment
   variables to an already-created container. Stop and recreate it with
   `--env-file` or `-e`:

   ```bash
   docker rm -f ml-workspace
   docker run -d --name ml-workspace -p 8080:8080 \
     --env-file .env ankitsurana/student-ml-env:latest
   ```

2. **Configuration files:** Mount a host directory or file into the
   workspace, then applications can read it without rebuilding the image:

   ```bash
   mkdir -p config
   docker run -d --name ml-workspace -p 8080:8080 \
     -v "$PWD/config:/workspace/config" \
     ankitsurana/student-ml-env:latest
   ```

   Put application configuration in `/workspace/config` and have your code
   read it from there. This is the best option when users need to edit
   settings from inside the running instance.

3. **One-off commands:** For a temporary value, pass it only to a command:

   ```bash
   docker exec -e OPENAI_API_KEY="$OPENAI_API_KEY" \
     ml-workspace ml-env python /workspace/projects/example.py
   ```

   This value is available to that process and is not persisted.

Do not expose code-server to the public internet without adding
authentication and TLS. The default `--auth none` behavior is intended for
localhost-only development.

## Build locally

Use the repository setup helper:

```bash
python3 setup.py       # macOS/Linux
python setup.py        # Windows
```

Or run the shell helper on macOS/Linux, Git Bash, or WSL:

```bash
bash setup.sh
```

Manual build:

```bash
docker compose build ml-ide
docker compose up -d ml-ide
```

See `COMMANDS.md` for lifecycle and service commands and `INSTALL.md` for
platform-specific installation notes.
