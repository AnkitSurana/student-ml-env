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

Publish additional service ports if you will launch those services later from
inside the same container:

```bash
docker run -d --name ml-workspace \
  -p 8080:8080 -p 8888:8888 -p 6006:6006 -p 8501:8501 -p 5000:5000 \
  ankitsurana/student-ml-env:latest
```

Then launch them without rebuilding:

```bash
docker exec -it ml-workspace ml-env jupyter
docker exec -it ml-workspace ml-env tensorboard
docker exec -it ml-workspace ml-env streamlit /workspace/projects/app.py
docker exec -it ml-workspace ml-env mlflow
```

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

You can also set values after entering the running container:

```bash
docker exec -it ml-workspace ml-env shell
export OPENAI_API_KEY='your-key'
export MODEL_NAME='local-model'
ml-env python /workspace/projects/example.py
```

## Compose with the complete environment

Clone the repository when you want persistent bind mounts and database
containers:

```bash
git clone https://github.com/AnkitSurana/student-ml-env.git
cd student-ml-env
docker compose up -d
```

This starts one complete Compose environment. Docker may show several
containers internally, but users manage them as one project on the shared
`ml-network`:

```bash
docker compose exec ml-ide ml-env jupyter
docker compose ps
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
