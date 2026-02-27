[![Binder](https://2i2c.mybinder.org/badge_logo.svg)](https://2i2c.mybinder.org/v2/gh/alxbilger/SOFA.tutorials/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2F000_config.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/alxbilger/SOFA.tutorials/blob/master/notebooks/000_config.ipynb)
[![CI](https://github.com/alxbilger/SOFA.tutorials/actions/workflows/ci.yml/badge.svg)](https://github.com/alxbilger/SOFA.tutorials/actions/workflows/ci.yml)

# SOFA Tutorials (Jupyter Notebooks)

A progressive learning path to get started with [SOFA](https://www.sofa-framework.org/) — an open-source framework for multi-physics simulation — using Python within Jupyter notebooks.

## Table of Contents
- [What this repository contains](#what-this-repository-contains)
- [Try it online (Binder / nbviewer)](#try-it-online)
- [Run locally (Clone and Install)](#run-locally)
- [Installation options](#installation-options) ([Conda](#option-a--conda-recommended), [Pip](#option-b--pip-system-python-or-virtualenv))
- [Getting started (launching notebooks)](#getting-started)
- [Troubleshooting](#troubleshooting)
- [Tests](#tests)
- [Creating new notebooks](#creating-new-notebooks)
- [Contributing and feedback](#contributing-and-feedback)

## What this repository contains
This repository hosts a curated sequence of Jupyter notebooks that introduce SOFA concepts step-by-step, from initial setup to building simple simulations and visualization. These notebooks are designed to be run interactively.

### Notebook Validation
To ensure the tutorials remain functional as SOFA evolves, this repository includes a **Notebook Validation System**. The test suite:
- Scans the `notebooks` directory for all `.ipynb` files.
- Converts notebooks to Python scripts using `jupytext`.
- Executes the converted scripts and tracks any SOFA-related errors or warnings.
- Skips code cells tagged with `active-ipynb` (typically used for interactive UI elements that cannot run in a headless environment).

## Try it online
The easiest way to explore these tutorials without installing anything is to use the online options:

- **Interactive (Binder)**: Launch an interactive environment where you can run and modify the notebooks.
  [![Binder](https://2i2c.mybinder.org/badge_logo.svg)](https://2i2c.mybinder.org/v2/gh/alxbilger/SOFA.tutorials/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2F000_config.ipynb)

- **Read-only (nbviewer)**: Quickly view the notebooks and their outputs without running them.
  [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/alxbilger/SOFA.tutorials/blob/master/notebooks/000_config.ipynb)

## Run locally
If you want to run the notebooks on your machine, first clone the repository:

```bash
git clone https://github.com/alxbilger/SOFA.tutorials.git
cd SOFA.tutorials
```

### Installation options

Choose one of the following options based on your preference. **Option A (Conda) is recommended** for beginners as it handles the SOFA installation for you.

#### Option A — Conda (Recommended)
This method creates an isolated environment and installs all Python dependencies, including the `sofa-python3` package.

**Prerequisite**: [Conda](https://docs.conda.io/en/latest/miniconda.html) (or [Mamba](https://mamba.readthedocs.io/)) must be installed.

1. **Create the environment**:
   ```bash
   conda env create -f environment.yml
   ```
2. **Activate the environment**:
   ```bash
   conda activate my-environment
   ```
3. **Verify the installation**:
   Ensure `sofa-python3` is present in the environment:
   ```bash
   # Windows (PowerShell/cmd)
   conda list | findstr /I sofa-python3
   # macOS/Linux
   conda list | grep -i sofa-python3
   ```

#### Option B — Pip (System Python or Virtualenv)
Use this option if you prefer using `pip` or already have SOFA installed on your system.

**Important**: This method only installs the Python dependencies. **You must install SOFA and its Python plugin separately.** See the official [SOFA installation guide](https://sofa-framework.github.io/doc/getting-started/binaries/binaries-instructions/).

1. **(Optional) Create a virtual environment**:
   - **Windows**: `python -m venv .venv; .venv\Scripts\Activate.ps1`
   - **macOS / Linux**: `python -m venv .venv; source .venv/bin/activate`

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Getting started
Once your environment is set up and activated, launch Jupyter:

```bash
# Ensure your environment is activated before running this
jupyter notebook
```

Alternatively, you can open the notebooks directly in **VS Code** (with the Jupyter extension installed) or **JupyterLab**.

**Next steps**:
1. Open the file `notebooks/000_config.ipynb`.
2. Follow the instructions within to verify your SOFA setup.
3. Progress through the notebooks sequentially (010, 020, etc.).

## Troubleshooting
- **`ImportError` related to `Sofa`**:
  - **Pip/Virtualenv**: Ensure SOFA is installed separately and that its `site-packages` are in your `PYTHONPATH`.
  - **Conda**: Verify the environment is activated and `sofa-python3` is listed in `conda list`.
- **`jupyter` command not found**: Ensure your environment is activated. If it still fails, install it via `pip install jupyter` or `conda install jupyter`.
- **3D widgets not rendering (e.g., `k3d`, `bokeh`)**:
  - Ensure your browser supports WebGL.
  - Refresh the page or restart the kernel.
  - Check if the required Jupyter extensions are enabled (`jupyter nbextension list`).

## Tests
To verify that all notebooks are still functional, run the test suite from the project root:

```bash
python -m unittest tests.run_tests -v
```

## Creating new notebooks
Contributions are welcome! If you want to add a new tutorial:

1. **Location**: Place the `.ipynb` file in the `notebooks/` directory.
2. **Naming**: Use the `XXX_name.ipynb` convention (e.g., `140_advanced_physics.ipynb`).
3. **Cell Tagging**: If your notebook contains interactive cells (like 3D widgets or buttons) that would hang or fail in a headless test environment, you **must tag them** with `active-ipynb`.
   - In Jupyter Notebook: `View -> Cell Toolbar -> Tags`. Enter `active-ipynb` in the text box for the specific cell.
   - In VS Code: Click on the "Tags" button in the cell toolbar.
4. **Validation**: Ensure your notebook passes the test suite before submitting:
   ```bash
   python -m unittest tests.run_tests -v
   ```

## Contributing and feedback
- **Feedback**: If you find bugs or have suggestions, please [open an issue](https://github.com/alxbilger/SOFA.tutorials/issues).
- **Pull Requests**: Improvements to existing notebooks or new tutorials are highly appreciated!
- **Links**: If you notice any broken links, please report them.
