# Installation

## Docker Hub image

Install Docker Desktop (Windows/macOS) or Docker Engine and Compose (Linux).
The image does not require API keys or a repository checkout for the IDE:

```bash
docker run -d --name ml-workspace \
  -p 8080:8080 \
  -v "$PWD/projects:/workspace/projects" \
  -v "$PWD/notebooks:/workspace/notebooks" \
  ankitsurana/student-ml-env:latest
```

Open http://localhost:8080.

To add optional provider keys, supply them at runtime. They are never stored
in the image:

```bash
docker run -d --name ml-workspace \
  -p 8080:8080 \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  ankitsurana/student-ml-env:latest
```

For several values, use a private file:

```bash
docker run -d --name ml-workspace -p 8080:8080 \
  --env-file .env ankitsurana/student-ml-env:latest
```

## Compose with optional databases

Clone the repository when you want persistent bind mounts and database
containers:

```bash
git clone https://github.com/AnkitSurana/student-ml-env.git
cd student-ml-env
docker compose up -d ml-ide
```

The default command starts only code-server. Start JupyterLab from the IDE
container or start database profiles when needed:

```bash
docker compose exec ml-ide ml-env jupyter
docker compose --profile database up -d
docker compose --profile vector up -d
```

No `.env` file is required. Copy `.env.example` to `.env` only when you want
to set optional keys or override ports and local database credentials.

## Local build

```bash
python3 setup.py
# or
bash setup.sh
```

The setup helpers build the image and start code-server without pausing for
credentials. See `COMMANDS.md` for service and lifecycle commands.
