FROM python:3.11-slim

ARG CODE_SERVER_VERSION=4.95.3

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    JUPYTER_CONFIG_DIR=/workspace/.jupyter \
    HOME=/workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ffmpeg \
    git \
    graphviz \
    libsm6 \
    libxext6 \
    libxrender-dev \
    nodejs \
    npm \
    tini \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt && \
    python -m spacy download en_core_web_sm && \
    python -m spacy download en_core_web_md && \
    npm install --global "code-server@${CODE_SERVER_VERSION}" && \
    npm cache clean --force

COPY docker/ml-env /usr/local/bin/ml-env
RUN chmod +x /usr/local/bin/ml-env && \
    mkdir -p /workspace/.jupyter /workspace/data /workspace/datasets /workspace/models /workspace/notebooks /workspace/projects && \
    printf '%s\n' \
      "c.ServerApp.ip = '0.0.0.0'" \
      "c.ServerApp.port = 8888" \
      "c.ServerApp.open_browser = False" \
      "c.ServerApp.allow_root = True" \
      "c.ServerApp.token = ''" \
      "c.ServerApp.password = ''" \
      "c.ServerApp.allow_origin = '*'" \
      > /workspace/.jupyter/jupyter_server_config.py

EXPOSE 8080 8888 5000 6006 8501

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "--disable-telemetry", "/workspace"]
