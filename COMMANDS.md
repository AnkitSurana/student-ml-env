# Command reference

## Start the IDE

```bash
docker compose up -d ml-ide
```

Open [VS Code](http://localhost:8080). The default image has no login token
because the port is published to localhost only.

## Launch services from inside the container

The image includes `ml-env`, so services can be started directly after opening
a shell in the running container:

```bash
docker exec -it ml-workspace ml-env help
docker exec -it ml-workspace ml-env jupyter
docker exec -it ml-workspace ml-env tensorboard
docker exec -it ml-workspace ml-env streamlit /workspace/projects/app.py
docker exec -it ml-workspace ml-env mlflow
```

The corresponding URLs are JupyterLab on `8888`, TensorBoard on `6006`,
Streamlit on `8501`, and MLflow on `5000`. The ports must be published when
the container is created.

To set optional keys from inside the instance, open a shell and export them
before launching the application:

```bash
docker exec -it ml-workspace ml-env shell
export OPENAI_API_KEY='your-key'
export POSTGRES_HOST=postgres
ml-env python /workspace/projects/example.py
```

These exports are inherited by commands started from that shell. They are
temporary and disappear when the container is recreated; use `docker run -e`,
`--env-file`, or Compose `.env` for persistent container configuration.

Run JupyterLab directly in the IDE container:

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
