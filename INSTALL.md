# 📥 Installation Guide

## Quick Start

```bash
# All OS
python setup.py

# Or Mac/Linux
bash setup.sh
```

## Windows Setup

1. Install Docker Desktop: https://www.docker.com/products/docker-desktop
2. Enable WSL2 when prompted
3. Restart computer
4. Clone repo: `git clone https://github.com/your-org/student-ml-env.git`
5. Run: `python setup.py`

## macOS Setup

1. Install Docker Desktop: https://www.docker.com/products/docker-desktop
2. Launch Docker from Applications
3. Clone repo: `git clone https://github.com/your-org/student-ml-env.git`
4. Run: `python3 setup.py`

## Linux Setup

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker

# Clone & setup
git clone https://github.com/your-org/student-ml-env.git
cd student-ml-env
python3 setup.py
```

## Troubleshooting

**Docker not found**: Install Docker Desktop first

**Port in use**: Edit docker-compose.yml and change ports

**Out of memory**: Increase Docker resources (4GB+ RAM, 20GB+ disk)

**Containers won't start**: Run `docker-compose logs` to view errors

See INSTALL.md for detailed guides.
