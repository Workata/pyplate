# basic-python-project-template
Template for a standard python project using github's CI/CD and devcontainers (VS code)

## About the project
Dummy structure template for a simple (non-framework related) python project. The point of this repo is to have a basic devcontainer and CI/CD setup. It should be later on adjusted according to the needs of specific project.

## Things you would want to replace/update

### setup.py

Update information about the project like Author, Description etc.

<!-- Linter/Formatter/Tests--->

## Things you would want to add

### Poetry

[Poetry](https://python-poetry.org/) can help you with packaging and dependency management.

<!-- ### CI/CD

#### Linter -->


## Development

### Setup project

* Create/copy config file:
```sh
cp config_example.yaml config.yaml
```

* Change config settings if needed

* Create venv
```sh
python3 -m venv ./venv
```

* Activate venv
```sh
. ./venv/bin/activate
```

* Install libs
```sh
pip install -r ./requirements/dev.txt
```

* Run program
```py
python3 ./src/main.py
```

### Format code

* Formatter (black)
```sh
black ./src/
```

### Test code

* Type checker (mypy)
```sh
mypy ./src/
```

* Linter (flake8)
```sh
flake8 ./src/
```

* Unit tests (pytest)
```sh
python3 -m pytest ./src/tests/
```

*Note: To format and test code with one command use:*
```sh
. ./scripts/run_checks.sh
```
