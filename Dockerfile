FROM python:3.11-slim

# Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    vim \
    ffmpeg \
    libsm6 \
    libxext6 \
    libxrender-dev \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Download spacy models
RUN python -m spacy download en_core_web_sm && \
    python -m spacy download en_core_web_md

# Configure Jupyter
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_origin = '*'" >> ~/.jupyter/jupyter_notebook_config.py

# Create directories
RUN mkdir -p /workspace/data /workspace/models /workspace/chroma_data

EXPOSE 8888 6006 5000 8501

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
