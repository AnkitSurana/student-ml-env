# Docker Hub command reference

These commands use one Docker container. No Docker Compose installation is
required for end users.

## Start and inspect

```bash
docker pull ankitsurana/student-ml-env:latest
docker run -d --name ml-workspace --restart unless-stopped \
  -p 8080:8080 -p 8888:8888 -p 5000:5000 -p 6006:6006 -p 8501:8501 \
  -v "$PWD/projects:/workspace/projects" \
  ankitsurana/student-ml-env:latest
docker ps
docker logs -f ml-workspace
```

Open VS Code at `http://localhost:8080`.

## Start tools

```bash
docker exec -it ml-workspace ml-env jupyter
docker exec -it ml-workspace ml-env tensorboard
docker exec -it ml-workspace ml-env mlflow
docker exec -it ml-workspace ml-env streamlit /workspace/projects/app.py
docker exec -it ml-workspace ml-env shell
docker exec ml-workspace ml-env python script.py
docker exec ml-workspace ml-env help
```

## Configure runtime values

At creation time:

```bash
docker run -d --name ml-workspace \
  --env OPENAI_API_KEY="$OPENAI_API_KEY" \
  --env POSTGRES_HOST=db.example.internal \
  --env POSTGRES_PORT=5432 \
  -p 8080:8080 -v "$PWD/projects:/workspace/projects" \
  ankitsurana/student-ml-env:latest
```

From an env file:

```bash
docker run -d --name ml-workspace --env-file .env \
  -p 8080:8080 -v "$PWD/projects:/workspace/projects" \
  ankitsurana/student-ml-env:latest
```

For a one-off command:

```bash
docker exec -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  ml-workspace ml-env python /workspace/projects/example.py
```

## Lifecycle

```bash
docker stop ml-workspace
docker start ml-workspace
docker restart ml-workspace
docker rm -f ml-workspace
```

## Developer-only Compose commands

Compose is retained for repository contributors who need bundled databases:

```bash
docker compose config
docker compose build ml-ide
docker compose up -d
docker compose ps
docker compose logs -f ml-ide
docker compose down
```

The Docker Hub user path does not use these commands. See `README.md` for
service boundaries and `INSTALL.md` for local development.
