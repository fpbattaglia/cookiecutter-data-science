# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/drivendata/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02.png)](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
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
```


## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
