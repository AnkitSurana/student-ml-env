# Command reference

## Start the IDE

```bash
docker compose up -d ml-ide
```

Open [VS Code](http://localhost:8080). The default image has no login token
because the port is published to localhost only.

## Launch services on demand

Run JupyterLab in the IDE container:

```bash
docker compose exec ml-ide ml-env jupyter
```

Then open [JupyterLab](http://localhost:8888). Stop it with `Ctrl-C` in the
attached command or use `docker compose exec ml-ide pkill -f 'jupyter lab'`.

Start database groups only when needed:

```bash
docker compose --profile database up -d     # PostgreSQL, MongoDB, Redis
docker compose --profile vector up -d       # Chroma, Qdrant, Weaviate, Milvus
docker compose --profile admin up -d        # pgAdmin and Mongo Express
```

Run a single service:

```bash
docker compose --profile database up -d postgres
docker compose --profile vector up -d qdrant
```

From Python, use the Compose service names (`postgres`, `mongodb`, `redis`,
`chromadb`, `qdrant`, `weaviate`, and `milvus`) as hostnames.

## Runtime keys

Keys are optional. Supply them without changing the image:

```bash
docker compose run --rm \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  ml-ide ml-env python script.py
```

Or create a private `.env` from `.env.example` and run Compose normally. For a
direct Docker Hub run, use `--env-file`:

```bash
docker run --rm -p 8080:8080 --env-file .env \
  -v "$PWD/projects:/workspace/projects" \
  ankitsurana/student-ml-env:latest
```

## Lifecycle

```bash
docker compose ps
docker compose logs -f ml-ide
docker compose down
```
