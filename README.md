# 🚀 Complete ML/AI Docker Environment

A **production-ready**, **OS-independent** Docker-based machine learning and AI development environment with Jupyter Lab, 200+ ML/AI libraries, and multiple vector databases.

Perfect for students, researchers, and ML practitioners.

---

## ✨ Features

✅ **200+ ML/AI Libraries** - TensorFlow, PyTorch, scikit-learn, XGBoost, LightGBM, etc.
✅ **Generative AI** - LangChain, LlamaIndex, CrewAI, Transformers
✅ **5 Vector Databases** - ChromaDB, Qdrant, Weaviate, Milvus, Pinecone
✅ **3 SQL/NoSQL Databases** - PostgreSQL, MongoDB, Redis
✅ **Jupyter Lab** - Interactive notebooks with git integration
✅ **Admin Interfaces** - pgAdmin, Mongo Express
✅ **Cross-Platform** - Windows, macOS, Linux (with WSL2)

---

## 📋 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 4 GB | 8 GB |
| **Disk** | 20 GB | 30 GB |
| **Docker** | Latest | Latest |

### Supported OS
- ✅ Windows 10/11 (with WSL2)
- ✅ macOS (Intel & Apple Silicon)
- ✅ Linux (Ubuntu, Fedora, Debian)

---

## 🚀 Prerequisites by Operating System

### 🪟 **Windows 10/11 Setup (DETAILED)**

#### Prerequisites Checklist
- [ ] Windows 10 Build 19041+ or Windows 11
- [ ] Administrator access (required)
- [ ] ~40 GB free disk space
- [ ] Internet connection (1+ Gbps recommended)
- [ ] Allow 45-60 minutes total (first time setup)

---

#### Step 1: Install Git for Windows

**Why?** Git is needed to clone (download) this repository from GitHub.

**Instructions:**

1. Open browser and go to: https://git-scm.com/download/win
2. Click the download link (automatic download starts)
3. Find the downloaded file `Git-xxxx-64-bit.exe` in Downloads folder
4. **Double-click** the installer
5. Windows will ask "Do you want to allow this app to make changes?" → Click **Yes**
6. Welcome screen appears → Click **Next**
7. Choose installation location → Click **Next** (default is fine)
8. Select components → Click **Next** (defaults are fine)
9. Choose start menu folder → Click **Next**
10. Select default editor → Click **Next** (Vim is fine)
11. Choose PATH environment → Select **"Git from the command line..."** → Click **Next**
12. Choose SSH executable → Click **Next** (default is fine)
13. Choose CRLF handling → Click **Next** (default is fine)
14. Choose terminal emulator → Click **Next** (defaults are fine)
15. Choose git pull behavior → Click **Next** (defaults are fine)
16. Click **Install** → Wait for installation to complete
17. Uncheck "View Release Notes" → Click **Finish**
18. **Restart your terminal/PowerShell completely** (close and reopen)

**Verify Installation:**
```powershell
git --version
```

Should show: `git version 2.xxx.x` (version number may differ)

If you get "command not found", restart your computer.

---

#### Step 2: Enable WSL2 (Windows Subsystem for Linux 2)

**Why?** Docker Desktop on Windows requires WSL2 to run Linux containers.

**Instructions:**

1. Right-click **PowerShell** → Select **Run as administrator**
2. Paste this command:
```powershell
wsl --install
```
3. Press **Enter**
4. Installation will start. You'll see output like:
   - "Installing Windows Subsystem for Linux..."
   - "Downloading Linux kernel..."
   - "Setting up WSL2..."
5. **This will take 5-10 minutes** - be patient, let it finish
6. When done, you'll see: "Installation successful!"
7. **Close PowerShell and RESTART YOUR COMPUTER** (this is important!)
8. After restart, open PowerShell again (normal, not admin)

**Verify Installation:**
```powershell
wsl --list --verbose
```

You should see something like:
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

If VERSION shows "1" instead of "2", run:
```powershell
wsl --set-default-version 2
```

---

#### Step 3: Install Docker Desktop for Windows

**Why?** Docker runs all the ML/AI services (Jupyter, databases, etc.) in isolated containers.

**Instructions:**

1. Open browser and go to: https://www.docker.com/products/docker-desktop
2. Click **Download for Windows** button
3. File `Docker Desktop Installer.exe` downloads
4. Find it in Downloads folder
5. **Double-click** the installer
6. Windows asks "Do you want to allow this app?" → Click **Yes**
7. Docker Desktop installer opens
8. Check the box: ☑️ **"Install required Windows components for WSL 2"**
9. Click **OK**
10. Installation starts (~2-3 minutes)
11. You'll see "Installing required Windows components..."
12. When complete, click **Restart** (Docker needs this)
13. **Computer will restart**
14. After restart, Docker Desktop should auto-launch from system tray
15. Wait for the Docker icon in bottom-right to show "Docker is running"
   - Icon is in the system tray (bottom-right corner)
   - If not visible, click the ^ arrow to show hidden icons
   - You'll see the Docker whale icon
   - Small circle next to it should be GREEN

**Verify Installation:**

Open PowerShell and run:
```powershell
docker --version
```

Should show: `Docker version 20.x.x` (version number may differ)

Then run:
```powershell
docker run hello-world
```

This downloads a small test image and runs it. You should see:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

If you get permission errors, restart computer.

---

#### Step 4: Clone This Repository

**Why?** You need to download this repository from GitHub to get all the files.

**Instructions:**

1. Open **PowerShell** (not admin, regular PowerShell)
2. Navigate to where you want the folder. Examples:
   - Desktop: `cd Desktop`
   - Documents: `cd Documents`
   - Home: `cd ~`
3. Run this command (copy-paste it):
```powershell
git clone https://github.com/your-org/student-ml-env.git
```
(Replace `your-org` with the actual GitHub organization/username)

4. Wait for it to finish. You'll see:
   ```
   Cloning into 'student-ml-env'...
   remote: Counting objects: xxx
   remote: Compressing objects: xxx
   ...
   done.
   ```

5. Navigate into the folder:
```powershell
cd student-ml-env
```

6. List contents to verify:
```powershell
dir
```

You should see files like:
```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         9/1/2024   4:00 PM                utils
-a----         9/1/2024   4:00 PM           1105 Dockerfile
-a----         9/1/2024   4:00 PM           3737 docker-compose.yml
-a----         9/1/2024   4:00 PM           3112 requirements.txt
-a----         9/1/2024   4:00 PM           4757 README.md
-a----         9/1/2024   4:00 PM           3650 setup.py
... (and more files)
```

---

#### Step 5: Configure Environment Variables

**Why?** Some features need API keys (optional but recommended). This file keeps them safe.

**Instructions:**

1. In PowerShell (inside `student-ml-env` folder), run:
```powershell
copy .env.example .env
```

2. Open the `.env` file with Notepad:
```powershell
notepad .env
```

3. You'll see a file with lines like:
```
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
```

4. If you have API keys:
   - Find the line with the API name
   - Replace `your-key-here` with your actual key
   - Example: `OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx`

5. If you don't have keys, leave defaults - everything still works

6. Save the file: Press `Ctrl+S`

7. Close Notepad

---

#### Step 6: Run the Setup Script

**Why?** This script automates everything: creates folders, builds Docker image, starts services.

**Instructions:**

1. Back in PowerShell (inside `student-ml-env` folder), run:
```powershell
python setup.py
```

2. You'll see:
```
==================================================
ML/AI Environment Setup
OS: Windows
==================================================

📁 Creating directories...
   ✓ notebooks
   ✓ data
   ... (more folders)
✅ Done

🐳 Checking Docker...
   ✓ Docker version 20.x.x
✅ Docker found
```

3. Script will ask:
```
⚙️  Setting up .env file...
   ✓ Created from template
   ⚠️  Edit .env and add your API keys
   Command: notepad .env

   Press Enter when done...
```

If you already have an `.env` file, just press **Enter**.

4. Building Docker image (~5-10 minutes on first run):
```
📦 Building Docker image...
   (First build: 5-8 minutes, uses cache afterwards)

Step 1/10 : FROM python:3.11-slim
...
Successfully built xxxxxxxx
✅ Docker image built successfully
```

Be patient! This downloads everything and sets it up.

5. Starting services (~1 minute):
```
🎬 Starting services...
✅ Services started

==================================================
✅ SETUP COMPLETE!
==================================================

📊 SERVICES RUNNING:

   • Jupyter Lab           http://localhost:8888
   • TensorBoard           http://localhost:6006
   • ChromaDB              http://localhost:8000
   • PostgreSQL            localhost:5432
   ... (more services)

🔑 GET JUPYTER TOKEN:
   PowerShell: docker-compose logs ml-jupyter | Select-String "token="

🎉 Setup complete! Open Jupyter at: http://localhost:8888

==================================================
```

---

#### Step 7: Access Jupyter Lab

**Instructions:**

1. Get your Jupyter token. In PowerShell, run:
```powershell
docker-compose logs ml-jupyter | Select-String "token="
```

2. You'll see output like:
```
jupyter_1  | To access the notebook, open this file in a browser:
jupyter_1  |     file:///root/.jupyter/jupyter_notebook_config.json
jupyter_1  | Or copy and paste one of these URLs:
jupyter_1  |     http://127.0.0.1:8888/?token=abcdef123456xyz789
```

3. Copy the full token value (the long string after `token=`)

4. Open your browser and go to: http://localhost:8888

5. Paste your token when prompted

6. Click **Login**

7. You're in Jupyter Lab! 🎉

**You're done with Windows setup!**

---

### 🍎 **macOS Setup (DETAILED)**

#### Prerequisites Checklist
- [ ] macOS 11 (Big Sur) or newer
- [ ] Administrator access (you'll be asked for password)
- [ ] ~40 GB free disk space
- [ ] Internet connection (1+ Gbps recommended)
- [ ] Allow 45-60 minutes total (first time setup)

---

#### Step 1: Install Git

**Option A: Using Homebrew (RECOMMENDED - Easier)**

1. Open **Terminal** (Applications → Utilities → Terminal)
2. Copy-paste this command:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Press **Enter**
4. Terminal will ask for your **password** (Mac login password)
5. Type your password and press **Enter** (you won't see the characters - this is normal)
6. Homebrew installs (~2-3 minutes)
7. When done, close Terminal

8. Open Terminal again (fresh Terminal window)
9. Install Git:
```bash
brew install git
```
10. Press **Enter**
11. Wait for installation to complete (~1 minute)

**Verify Installation:**
```bash
git --version
```
Should show: `git version 2.xxx.x`

---

**Option B: Direct Download (If Homebrew doesn't work)**

1. Open browser and go to: https://git-scm.com/download/mac
2. Download link appears automatically (might be labeled "Download 2.x.x")
3. Open Downloads folder → find `git-xxxx.dmg` file
4. Double-click it
5. Installer disk mounts (appears as a disk on desktop)
6. Double-click the `Git Installer` file
7. Mac asks "Are you sure?" → Click **Open**
8. Follow installer prompts:
   - Click **Continue**
   - Select destination → Click **Install**
   - Enter your **Mac password**
   - Click **Install Software**
   - Click **Close** when done
9. Right-click the disk on desktop → Click **Eject**

**Verify Installation:**
```bash
git --version
```

---

#### Step 2: Install Docker Desktop for Mac

**Why?** Docker runs all the ML/AI services (Jupyter, databases, etc.).

**First, check your Mac chip:**
- Click Apple logo (top-left) → **About This Mac**
- Look for "Chip:"
  - If it says "Apple Silicon" (M1, M2, M3, M4) → Use ARM64 version
  - If it says "Intel Core" → Use Intel version

**For Apple Silicon (M1/M2/M3/M4):**

1. Open browser: https://desktop.docker.com/mac/main/arm64/Docker.dmg
2. File `Docker.dmg` downloads
3. Open Downloads folder → Double-click `Docker.dmg`
4. Disk mounts (appears on desktop)
5. Two icons appear: Docker.app and Applications folder
6. **Drag** Docker.app to Applications folder
   - Hold click on Docker.app
   - Drag it to Applications
   - Release
   - Wait for copy to complete (~30 seconds)
7. Right-click Docker.dmg disk → **Eject**
8. Open Applications folder (Finder → Applications)
9. Find Docker.app → Double-click it
10. Mac asks for password → Enter your **Mac password** → Click **OK**
11. Docker launches
12. Wait for Docker icon in menu bar (top-right)
    - Look for whale icon
    - Should show "Docker is running"
    - Wait 1-2 minutes

**For Intel Mac:**

Same as above but use: https://desktop.docker.com/mac/main/amd64/Docker.dmg

**Verify Installation:**

Open Terminal and run:
```bash
docker --version
```
Should show: `Docker version 20.x.x`

Then run:
```bash
docker run hello-world
```
Should see: "Hello from Docker!"

---

#### Step 3: Install Xcode Command Line Tools (if needed)

**Why?** Some tools need these to compile code.

**Check if you need it:**

Open Terminal and run:
```bash
xcode-select --install
```

If you get "xcode-select: error: command line tools are already installed", you're good!

If dialog appears asking to install, click **Install** and wait (~2-3 minutes).

---

#### Step 4: Clone This Repository

**Why?** You need to download this repository from GitHub to get all the files.

**Instructions:**

1. Open **Terminal**
2. Navigate to where you want the folder:
   - Desktop: `cd Desktop`
   - Documents: `cd Documents`
   - Home: `cd ~`
3. Run:
```bash
git clone https://github.com/your-org/student-ml-env.git
```
(Replace `your-org` with actual GitHub username/organization)

4. Wait for completion. You'll see:
```
Cloning into 'student-ml-env'...
remote: Counting objects: xxx
remote: Compressing objects: xxx
...
done.
```

5. Navigate into the folder:
```bash
cd student-ml-env
```

6. List contents to verify:
```bash
ls -la
```

You should see files like:
```
Dockerfile
docker-compose.yml
requirements.txt
setup.py
README.md
utils/
```

---

#### Step 5: Configure Environment Variables

**Why?** Some features need API keys (optional but recommended).

**Instructions:**

1. In Terminal (inside `student-ml-env` folder), run:
```bash
cp .env.example .env
```

2. Open the `.env` file:
```bash
nano .env
```

3. File opens in Terminal editor. You'll see:
```
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
...
```

4. If you have API keys:
   - Use arrow keys to navigate
   - Find the line with the API name
   - Replace `your-key-here` with your actual key
   - Example: `OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx`

5. If you don't have keys, leave defaults - everything still works

6. Save the file:
   - Press **Ctrl+X** (hold Control, press X)
   - Press **Y** (yes, save)
   - Press **Enter** (confirm filename)

7. You're done editing

---

#### Step 6: Run the Setup Script

**Why?** This script automates everything: creates folders, builds Docker image, starts services.

**Instructions:**

1. In Terminal (inside `student-ml-env` folder), run:
```bash
python3 setup.py
```

2. You'll see:
```
==================================================
ML/AI Environment Setup
OS: Darwin
==================================================

📁 Creating directories...
   ✓ notebooks
   ✓ data
   ... (more folders)
✅ Done

🐳 Checking Docker...
   ✓ Docker version 20.x.x
✅ Docker found
```

3. Script asks about `.env` file:
```
⚙️  Setting up .env file...
   ✓ Created from template
   ⚠️  Edit .env and add your API keys
   
   Press Enter when done...
```

If you already configured `.env`, just press **Enter**.

4. Building Docker image (~5-10 minutes on first run):
```
📦 Building Docker image...
   (First build: 5-8 minutes, uses cache afterwards)

Step 1/10 : FROM python:3.11-slim
...
Successfully built xxxxxxxx
✅ Docker image built successfully
```

**Be patient!** This downloads everything and sets it up.

5. Starting services (~1 minute):
```
🎬 Starting services...
✅ Services started

==================================================
✅ SETUP COMPLETE!
==================================================

📊 SERVICES RUNNING:

   • Jupyter Lab           http://localhost:8888
   • TensorBoard           http://localhost:6006
   • ChromaDB              http://localhost:8000
   • PostgreSQL            localhost:5432
   ... (more services)

🔑 GET JUPYTER TOKEN:
   Terminal: docker-compose logs ml-jupyter | grep token

==================================================
```

---

#### Step 7: Access Jupyter Lab

**Instructions:**

1. Get your Jupyter token. In Terminal, run:
```bash
docker-compose logs ml-jupyter | grep token
```

2. You'll see output like:
```
jupyter_1  | To access the notebook, open this file in a browser:
jupyter_1  |     file:///root/.jupyter/jupyter_notebook_config.json
jupyter_1  | Or copy and paste one of these URLs:
jupyter_1  |     http://127.0.0.1:8888/?token=abcdef123456xyz789
```

3. Copy the token value (long string after `token=`)

4. Open your browser and go to: http://localhost:8888

5. Paste your token when prompted

6. Click **Login**

7. You're in Jupyter Lab! 🎉

**You're done with macOS setup!**

---

### 🐧 **Linux Setup (Ubuntu/Debian) (DETAILED)**

#### Prerequisites Checklist
- [ ] Ubuntu 20.04+ or Debian 11+
- [ ] sudo access (password required for some commands)
- [ ] ~40 GB free disk space
- [ ] Internet connection (1+ Gbps recommended)
- [ ] Allow 45-60 minutes total (first time setup)

---

#### Step 1: Install Git

**Why?** Git is needed to clone (download) this repository from GitHub.

**Instructions:**

1. Open **Terminal** (Applications → Terminal, or Ctrl+Alt+T)
2. Update package list:
```bash
sudo apt update
```
3. Enter your **password** when prompted (you won't see characters - this is normal)
4. Wait for update to complete
5. Install Git:
```bash
sudo apt install -y git
```
6. Press **Enter**
7. Type your **password** if prompted
8. Wait for installation (~1 minute)

**Verify Installation:**
```bash
git --version
```
Should show: `git version 2.xxx.x`

---

#### Step 2: Install Docker Engine

**Why?** Docker runs all the ML/AI services (Jupyter, databases, etc.).

**Instructions:**

1. Open Terminal
2. Update packages:
```bash
sudo apt update
```
3. Enter your **password**
4. Install dependencies:
```bash
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
```
5. Enter your **password**
6. Add Docker's GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
7. Enter your **password**
8. Add Docker repository:
```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
9. Update package list again:
```bash
sudo apt update
```
10. Install Docker:
```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
11. Enter your **password**
12. Wait for installation (~3-5 minutes)
13. Start Docker service:
```bash
sudo systemctl start docker
```
14. Enable Docker to start on boot:
```bash
sudo systemctl enable docker
```
15. Add your user to docker group (so you don't need sudo every time):
```bash
sudo usermod -aG docker $USER
```
16. Enter your **password**
17. Activate group membership:
```bash
newgrp docker
```
18. Close and reopen Terminal (fresh login needed)

**Verify Installation:**
```bash
docker --version
```
Should show: `Docker version 20.x.x`

Then run:
```bash
docker run hello-world
```
Should see: "Hello from Docker!"

---

#### Step 3: Clone This Repository

**Why?** You need to download this repository from GitHub to get all the files.

**Instructions:**

1. Open **Terminal**
2. Navigate to where you want the folder:
   - Home: `cd ~`
   - Desktop: `cd ~/Desktop`
   - Documents: `cd ~/Documents`
3. Run:
```bash
git clone https://github.com/your-org/student-ml-env.git
```
(Replace `your-org` with actual GitHub username/organization)

4. Wait for completion. You'll see:
```
Cloning into 'student-ml-env'...
remote: Counting objects: xxx
remote: Compressing objects: xxx
...
done.
```

5. Navigate into the folder:
```bash
cd student-ml-env
```

6. List contents to verify:
```bash
ls -la
```

You should see files like:
```
Dockerfile
docker-compose.yml
requirements.txt
setup.py
README.md
utils/
```

---

#### Step 4: Configure Environment Variables

**Why?** Some features need API keys (optional but recommended).

**Instructions:**

1. In Terminal (inside `student-ml-env` folder), run:
```bash
cp .env.example .env
```

2. Open the `.env` file:
```bash
nano .env
```

3. File opens in Terminal editor. You'll see:
```
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
...
```

4. If you have API keys:
   - Use arrow keys to navigate
   - Find the line with the API name
   - Replace `your-key-here` with your actual key
   - Example: `OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx`

5. If you don't have keys, leave defaults - everything still works

6. Save the file:
   - Press **Ctrl+X** (hold Control, press X)
   - Press **Y** (yes, save)
   - Press **Enter** (confirm filename)

---

#### Step 5: Run the Setup Script

**Why?** This script automates everything: creates folders, builds Docker image, starts services.

**Instructions:**

1. In Terminal (inside `student-ml-env` folder), run:
```bash
python3 setup.py
```

2. You'll see:
```
==================================================
ML/AI Environment Setup
OS: Linux
==================================================

📁 Creating directories...
   ✓ notebooks
   ✓ data
   ... (more folders)
✅ Done

🐳 Checking Docker...
   ✓ Docker version 20.x.x
✅ Docker found
```

3. Script asks about `.env` file:
```
⚙️  Setting up .env file...
   ✓ Created from template
   ⚠️  Edit .env and add your API keys
   
   Press Enter when done...
```

If you already configured `.env`, just press **Enter**.

4. Building Docker image (~5-10 minutes on first run):
```
📦 Building Docker image...
   (First build: 5-8 minutes, uses cache afterwards)

Step 1/10 : FROM python:3.11-slim
...
Successfully built xxxxxxxx
✅ Docker image built successfully
```

**Be patient!** This downloads everything and sets it up.

5. Starting services (~1 minute):
```
🎬 Starting services...
✅ Services started

==================================================
✅ SETUP COMPLETE!
==================================================

📊 SERVICES RUNNING:

   • Jupyter Lab           http://localhost:8888
   • TensorBoard           http://localhost:6006
   • ChromaDB              http://localhost:8000
   • PostgreSQL            localhost:5432
   ... (more services)

🔑 GET JUPYTER TOKEN:
   Terminal: docker-compose logs ml-jupyter | grep token

==================================================
```

---

#### Step 6: Access Jupyter Lab

**Instructions:**

1. Get your Jupyter token. In Terminal, run:
```bash
docker-compose logs ml-jupyter | grep token
```

2. You'll see output like:
```
jupyter_1  | To access the notebook, open this file in a browser:
jupyter_1  |     file:///root/.jupyter/jupyter_notebook_config.json
jupyter_1  | Or copy and paste one of these URLs:
jupyter_1  |     http://127.0.0.1:8888/?token=abcdef123456xyz789
```

3. Copy the token value (long string after `token=`)

4. Open your browser and go to: http://localhost:8888

5. Paste your token when prompted

6. Click **Login**

7. You're in Jupyter Lab! 🎉

**You're done with Linux (Ubuntu/Debian) setup!**

---

### 🐧 **Linux Setup (Fedora/RHEL) (DETAILED)**

#### Prerequisites Checklist
- [ ] Fedora 35+ or RHEL 8+
- [ ] sudo access (password required)
- [ ] ~40 GB free disk space
- [ ] Internet connection (1+ Gbps recommended)
- [ ] Allow 45-60 minutes total (first time setup)

---

#### Step 1: Install Git

**Why?** Git is needed to clone (download) this repository.

**Instructions:**

1. Open **Terminal**
2. Update package list:
```bash
sudo dnf update -y
```
3. Enter your **password**
4. Wait for update (~1-2 minutes)
5. Install Git:
```bash
sudo dnf install -y git
```
6. Type your **password**
7. Wait for installation (~1 minute)

**Verify Installation:**
```bash
git --version
```

---

#### Step 2: Install Docker Engine

**Why?** Docker runs all the ML/AI services.

**Instructions:**

1. Open Terminal
2. Install Docker:
```bash
sudo dnf install -y docker
```
3. Enter your **password**
4. Wait for installation (~2-3 minutes)
5. Install Docker Compose:
```bash
sudo dnf install -y docker-compose
```
6. Enter your **password**
7. Start Docker service:
```bash
sudo systemctl start docker
```
8. Enable Docker to start on boot:
```bash
sudo systemctl enable docker
```
9. Add your user to docker group:
```bash
sudo usermod -aG docker $USER
```
10. Enter your **password**
11. Activate group membership:
```bash
newgrp docker
```
12. Close and reopen Terminal (fresh login needed)

**Verify Installation:**
```bash
docker --version
```

Should show: `Docker version 20.x.x`

---

#### Step 3-6: Clone and Run

**Same as Ubuntu/Debian steps above (Steps 3-6):**

1. Clone repository
2. Configure .env file
3. Run setup.py
4. Access Jupyter Lab

**You're done with Linux (Fedora/RHEL) setup!**

---

## 🚀 Quick Start (After Prerequisites Installed)

Once you have Git and Docker installed on your OS:

```bash
# 1. Clone
git clone https://github.com/your-org/student-ml-env.git
cd student-ml-env

# 2. Setup (automatic - just follow prompts)
python setup.py

# 3. Access Jupyter Lab
# Open browser: http://localhost:8888
```

**That's it!** 🎉

---

## ⚙️ What `setup.py` Does

When you run `python setup.py`, it automatically:
1. ✅ Creates workspace directories
2. ✅ Checks Docker installation
3. ✅ Sets up `.env` file
4. ✅ Builds Docker image (~5-10 minutes)
5. ✅ Starts all services (Jupyter, Vector DBs, SQL DBs)
6. ✅ Prints access information

---

## 📖 Getting the Jupyter Token

After setup, to access Jupyter Lab, you need a token:

**Windows PowerShell:**
```powershell
docker-compose logs ml-jupyter | Select-String "token="
```

**macOS/Linux:**
```bash
docker-compose logs ml-jupyter | grep token
```

Copy the token and paste it at: http://localhost:8888

---

## 📚 Documentation

- **[README.md](README.md)** - This file (overview)
- **[INSTALL.md](INSTALL.md)** - Detailed installation guides
- **[COMMANDS.md](COMMANDS.md)** - Docker commands reference
- **[SECURITY.md](SECURITY.md)** - Security best practices

---

## 📦 What's Included

### Deep Learning
- TensorFlow, Keras, PyTorch, PyTorch Lightning
- Torchvision, Torchaudio

### ML Models (ALL Algorithms)
- Regression, Classification, Clustering
- Dimensionality Reduction, Anomaly Detection
- XGBoost, LightGBM, CatBoost

### Generative AI & LLMs
- LangChain, LlamaIndex, CrewAI
- OpenAI, Anthropic, Google, Cohere
- RAG with Vector Databases

### NLP
- Transformers, spaCy, NLTK, Gensim
- Sentence Transformers for embeddings

### Computer Vision
- OpenCV, Pillow, YOLO, Albumentations

### Hyperparameter Tuning
- Optuna, Hyperopt, Ray Tune
- Bayesian Optimization

### Explainability
- SHAP, LIME, ELI5
- Permutation Importance

---

## 🔧 Configuration

### Environment Variables

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
nano .env  # Edit with your keys
```

### Using Configuration in Code

```python
from utils.config import Config

# Access variables
openai_key = Config.OPENAI_API_KEY
db_host = Config.POSTGRES_HOST

# Check LLM providers
status = Config.validate_llm_keys()
```

---

## 📊 Services

| Service | URL | Purpose |
|---------|-----|---------|
| **Jupyter Lab** | http://localhost:8888 | Interactive notebooks |
| **ChromaDB** | http://localhost:8000 | Local vector DB |
| **Qdrant** | http://localhost:6333 | Production vector DB |
| **Weaviate** | http://localhost:8080 | Enterprise vector DB |
| **Milvus** | http://localhost:19530 | Scalable vector DB |
| **PostgreSQL** | localhost:5432 | SQL database |
| **MongoDB** | localhost:27017 | NoSQL database |
| **Redis** | localhost:6379 | Cache/session store |
| **pgAdmin** | http://localhost:5050 | PostgreSQL manager |
| **Mongo Express** | http://localhost:8081 | MongoDB manager |

---

## 🐳 Docker Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f ml-jupyter

# Access shell
docker-compose exec ml-jupyter bash

# Get Jupyter token
docker-compose logs ml-jupyter | grep token
```

---

## 🎯 Use Cases

✅ Student learning ML/AI
✅ Data scientist prototyping
✅ ML engineer building models
✅ Researcher running experiments
✅ Educator distributing to courses
✅ Hackathon participant
✅ Anyone needing complete ML stack

---

## 📁 Directory Structure

```
student-ml-env/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── setup.py
├── .gitignore
├── utils/
│   ├── config.py
│   └── vector_db.py
├── notebooks/
├── data/
├── models/
└── projects/
```

---

## 🚀 Getting Help

1. Check [INSTALL.md](INSTALL.md) for OS-specific setup
2. View [COMMANDS.md](COMMANDS.md) for Docker commands
3. Review [SECURITY.md](SECURITY.md) for best practices
4. Check GitHub Issues if available

---

## 📄 License

MIT License - Use freely

---

## ✨ Next Steps

1. ✅ Install Docker Desktop
2. ✅ Clone or download repository
3. ✅ Run `python setup.py`
4. ✅ Edit `.env` with API keys
5. ✅ Open Jupyter Lab
6. ✅ Start building!

---

**Happy coding! 🚀**

Made for students and ML practitioners
