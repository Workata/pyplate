# pyplate
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

### Test code

On every commit code should be static tested/checked/formatted automatically (using [pre-commit](https://pre-commit.com/) tool). If you want to run static tests + unit tests run:

```sh
./scripts/run_tests.sh
```
