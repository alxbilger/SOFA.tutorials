[![Binder](https://2i2c.mybinder.org/badge_logo.svg)](https://2i2c.mybinder.org/v2/gh/alxbilger/SOFA.tutorials/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2F000_config.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/alxbilger/SOFA.tutorials/blob/master/notebooks/000_config.ipynb)

# SOFA Tutorials (Jupyter Notebooks)

A progressive learning path to get started with [SOFA](https://www.sofa-framework.org/) — a physics simulation engine — using Python in Jupyter notebooks.

## Table of Contents
- What this repository contains
- Use online (Binder / nbviewer)
- Run locally (clone and install)
- Installation options (pip, virtualenv, conda)
- Getting started (launch notebooks)
- Troubleshooting
- Contributing and feedback

## What this repository contains
This repository hosts a curated sequence of Jupyter notebooks that introduce SOFA concepts step by step, from initial setup to simple simulations and visualization. The notebooks are designed to be run interactively.

## Use online
You can view or run the notebooks online:

- Interactive (Binder):
  [![Binder](https://2i2c.mybinder.org/badge_logo.svg)](https://2i2c.mybinder.org/v2/gh/alxbilger/SOFA.tutorials/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2F000_config.ipynb)

- Read-only (nbviewer):
  [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/alxbilger/SOFA.tutorials/blob/master/notebooks/000_config.ipynb)

## Run locally
If you prefer running the notebooks on your machine:

```bash
git clone https://github.com/alxbilger/SOFA.tutorials.git
cd SOFA.tutorials
```

Then choose one of the installation options below and follow "Getting started".

## Installation options

### Option A — Conda (includes SOFA bindings)
This method creates an isolated Conda environment and installs Python dependencies plus the `sofa-python3` package from the SOFA channel.

Prerequisite: Conda must be installed and available on your PATH.

1) Create the environment from `environment.yml`:
```bash
conda env create -f environment.yml
```

2) Activate it (the default name is `my-environment`):
```bash
conda activate my-environment
```

3) Verify it appears in your environment list:
```bash
conda env list
```

If you run into issues importing SOFA in notebooks, confirm that `sofa-python3` is present:
```bash
conda list | findstr /I sofa-python3   # Windows (PowerShell/cmd)
# or
conda list | grep -i sofa-python3      # macOS/Linux
```

### Option B — Pip (system Python or virtualenv)
Install Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Note: this installs Python dependencies only. You still need a working SOFA installation separately. See the official [SOFA installation guide](https://sofa-framework.github.io/doc/getting-started/binaries/binaries-instructions/).

### Option C — Virtual environment
Using a virtual environment avoids conflicts with other Python packages.

- Windows (PowerShell):
  ```bash
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

- Windows (cmd.exe):
  ```batch
  python -m venv .venv
  .venv\Scripts\activate.bat
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

- macOS / Linux (bash/zsh):
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

Reminder: SOFA itself is not installed by `requirements.txt`. Install SOFA separately if you use pip/virtualenv.

## Getting started
Launch Jupyter from the project root:
```bash
# ensure "jupyter" is on your PATH (activating your env usually provides it)
jupyter notebooks
```
Alternative:
```bash
python -m jupyter notebooks
```

You can also open and run the notebooks in VS Code / VSCodium or JupyterLab.

Progress through the notebooks sequentially, starting with `notebook/000_config.ipynb`.

## Troubleshooting
- ImportError related to SOFA or `sofa-python3`:
  - If you used pip/virtualenv, ensure you installed SOFA separately and that the Python bindings are accessible.
  - If you used Conda, ensure `sofa-python3` is installed (see the check above) and that you activated the correct environment.
- Jupyter not found: confirm your environment is activated and `jupyter` is installed (`pip show jupyter` or `conda list jupyter`).
- Rendering issues with 3D widgets (e.g., `k3d`, `bokeh`): verify the corresponding packages are installed and that your browser supports WebGL.

## Tests

Run the test suite from the project root:
```bash
python -m unittest tests.run_tests -v
```

## Contributing and feedback
- Contributions (fixes, improvements, new notebooks) are welcome. Feel free to open issues or pull requests.
- If you notice broken links or installation problems, please open an issue with details about your OS and environment.
