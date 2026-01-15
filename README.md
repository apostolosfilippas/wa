# Web Analytics

## Description
This is the hands-on portion of our Web Analytics class
- We will be using Python 3.13
- We use **uv** for Python version management and package management


## Prerequisites

### 1. Install uv (Python Package Manager)

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart your terminal and verify:
```bash
uv --version
```

### 2. Clone this repository
```bash
git clone <repository-url>
cd wa
```

### 3. Install Python and dependencies
```bash
make install
```

This will:
- Install Python 3.13 (if not already installed)
- Create a virtual environment
- Install all required packages
- Install pre-commit hooks
- Register the Jupyter kernel


## Quick Reference

### Common Commands

```bash
# Install everything
make install

# Uninstall (remove venv and hooks)
make uninstall

# Add a new package
make add PKG=package-name

# Remove a package
make remove PKG=package-name

# Run a Python script
make run SCRIPT=scripts/example.py

# Start Jupyter notebook
make jupyter

# Format Python files with black
make format

# See all available commands
make help
```

### Running Python with uv

```bash
# Run a script
uv run python scripts/example.py

# Open Python REPL
uv run python

# Install a package
uv add package-name
```
