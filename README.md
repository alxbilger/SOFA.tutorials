[![Binder](https://2i2c.mybinder.org/badge_logo.svg)](https://2i2c.mybinder.org/v2/gh/alxbilger/SOFA.tutorials/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebook%2F000_config.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/alxbilger/SOFA.tutorials/blob/master/notebook/000_config.ipynb)

# SOFA Tutorial Series for Jupyter Notebooks

A progressive learning path for beginners to get started with [SOFA](https://www.sofa-framework.org/) (a physics simulation engine) using Python and Jupyter notebooks.

## How to use this repository

### Online

This notebook is available online using Binder:

[![Binder](https://2i2c.mybinder.org/badge_logo.svg)](https://2i2c.mybinder.org/v2/gh/alxbilger/SOFA.tutorials/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebook%2F000_config.ipynb)

This notebook is also available online (without interaction) using nbviewer:

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/alxbilger/SOFA.tutorials/blob/master/notebook/000_config.ipynb)

### Clone this repository

If you want to run the notebooks locally, clone this repository.

```bash
git clone https://github.com/alxbilger/SOFA.tutorials.git
```

Then, follow the instructions below to install the dependencies and run the notebooks.

## Install dependencies

### Pip 

```bash
pip install -r requirements.txt
```

It will install all the dependencies except SOFA. SOFA remains to be installed manually. See [SOFA installation guide](https://sofa-framework.github.io/doc/getting-started/binaries/binaries-instructions/).

### Virtual Environment

It is recommended to use a virtual environment to avoid conflicts with other Python packages.

#### Windows (PowerShell)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Windows (batch)

```batch
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### macOS / Linux (bash/zsh)

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### Conda

This method provides an isolated environment with all the dependencies, including SOFA.
Conda command line must be available.

1. Create the environment from the environment.yml file:

```bash
conda env create -f environment.yml
```

2. Activate the environment:

```bash
conda activate my-environment
```

3. Verify that the new environment was installed correctly:

```bash
conda env list
```

## Getting Started

Run notebooks with:
```bash
# make sure jupyter is in your PATH variable
jupyter notebook
```
Alternative:
```
python -m jupyter notebook
```

Or execute cells directly in VS Cod[e|ium] or JupyterLab.

Progress through the notebooks sequentially