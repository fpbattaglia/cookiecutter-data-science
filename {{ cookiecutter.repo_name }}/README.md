{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

_The overall description of the project goes here

Project Organization
------------

    ├── LICENSE            <- License file
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── intermediate   <- Directory tree for intermediate results  
    │   ├── preprocessed   <- Directory tree for preprocessed data (e.g. subsampled, spike sorted)
    │   ├── raw            <- Raw data directory (will be readonly)
    │   └── results        <- Directory for results and figures
    ├── docs               <- a Sphinx documentation project
    │   ├── Makefile
    │   ├── commands.rst
    │   ├── conf.py
    │   ├── getting-started.rst
    │   ├── index.rst
    │   └── make.bat
    ├── environment.yml   <- Conda environment specification, with standard packages
    ├── notebooks         <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references        <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports           <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures       <- Generated graphics and figures to be used in reporting
    ├── setup.py          <- makes project pip installable (pip install -e .) so src can be imported
    ├── src               <- Source code for use in this project.
    │   ├── __init__.py
    │   ├── analysis      <- Project-specific analysis code
    │   │   └── __init__.py
    │   ├── preprocessing <- Project-specific preprocessing code
    │   │   └── __init__.py
    │   └── visualization <- Project-specific visualization code
    │       ├── __init__.py
    │       └── visualize.py
    └── tox.ini          <- tox file with settings for running tox; see tox.testrun.org


 

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
