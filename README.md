![Workflow status](https://github.com/workata/pyplate/actions/workflows/checks.yml/badge.svg)

<p align="center">
  <img src="imgs/pyplate_logo.png" width="290" height="290" alt="pyplate logo"/>
</p>


Template for a standard python project using github's CI/CD and devcontainers (VS code)

## About the project
Dummy structure template for a simple (non-framework related) python project. The point of this repo is to have a basic devcontainer and CI/CD setup. It should be later on adjusted according to the needs of specific project.

### Integrated tools

- **[black](https://black.readthedocs.io/en/stable/)** (formatter)
- **[flake8](https://flake8.pycqa.org/en/latest/)** (linter)
- **[mypy](https://mypy.readthedocs.io/en/stable/)** (type checker)
- **[pytest](https://docs.pytest.org/en/7.1.x/contents.html)** (unit tests)
- **[pydantic](https://docs.pydantic.dev/latest/)** (settings/configs)
- **[pur](https://github.com/alanhamlett/pip-update-requirements)** (package updater)
- **[pre-commit](https://pre-commit.com/)**
- **[devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)**

## TODOs for developer after using this template

- [ ] Find and replace all occurrences of 'app-name' to your project name phrase.
- [ ] Open `setup.py` and update information about the project like Author, Description etc.
- [ ] Adjust (remove/add) tools and related configs according to your needs


## Other tools you would want to add

#### Poetry

[Poetry](https://python-poetry.org/) can help you with packaging and dependency management.

##### ...


<!-- ## Development -->

## Setup project

####  Setup with devcontainer (recommended)
This template project uses devcontainer (VS code) to setup everything. So just follow [official documentation](https://code.visualstudio.com/docs/devcontainers/tutorial) to meet prerequisites. Then open this template project in container (using VS code) and you are ready to code!

#### Setup without devcontainer

Copy env file
```sh
cp -n .env.example .env
```

Create new venv
```sh
python3 -m venv ./venv
```

Activate venv
```sh
. ./venv/bin/activate
```

Install needed requirements
```sh
pip install -r requirements/dev.txt
```

Run unit tests to check if it works
```sh
pytest ./src/
```

#### Pre-commit
[Pre-commit](https://pre-commit.com/) configuration is enabled for this project. To add the hook run the following command:

```sh
pre-commit install
```

## Test code

On every commit code should be static tested/checked/formatted automatically (using [pre-commit](https://pre-commit.com/) tool). If you want to run static tests + unit tests then run:

```sh
./scripts/run_tests.sh
```

## Update packages
You can manually run a script that will check for new versions of packages which are used in this project. It will update both requirements files (`base.txt`, `dev.txt`).

```sh
./scripts/update_packages.sh
```

On top of that there is a workflow added (`packages_update.yml`) that will create new Pull Request automatically with updated packages. Cronjob for this task is set for: `0 20 * * *` (every day - 20:00).

## Dockerize

There are two Dockerfiles in this project.

- `.devcontainer/Dockerfile`
- `Dockerfile`

First is for developing in a devcontainer and it's also used for running stuff in the pipeline. The second is for deploying the product as shown below. You should exclude unnecessary files (such as tests) using `.dockerignore` to keep the "production ready" container as ligthweight as possible.

Build image
```sh
docker build . --tag app-image
```

Create container and run it
```sh
docker run app-image
```
