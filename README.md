# basic-python-project-template
Template for a standard python project using github's CI/CD and devcontainers (VS code)

## About the project
Dummy structure template for a simple (non-framework related) python project. The point of this repo is to have a basic devcontainer and CI/CD setup. It should be later on adjusted according to the needs of specific project.

## Things you would want to replace/update

First of all, find and replace all occurrences of 'app-name' to your project name phrase.

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

This template project uses devcontainer (VS code) to setup everything. So just follow [official documentation](https://code.visualstudio.com/docs/devcontainers/tutorial) to meet prerequisites. Then open this template project in container (using VS code) and you are ready to code!

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
pytest ./src/tests/
```

*Note: To format and test code with one command use:*
```sh
. ./scripts/run_checks.sh
```
