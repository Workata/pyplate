[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/downloads/release/python-314/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![prek](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Contributions](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)
![PyPlate stars](https://img.shields.io/github/stars/workata/pyplate)


<p align="center">
  <img src="imgs/pyplate_logo_v2.png" width="320" height="320" alt="pyplate logo"/>
</p>


## About the project
Template for a standard (non-framework related) python project. The point of this repo is to have a basic project layout with working CI/CD <!-- , devcontainer --> and integrated common python tools. **It should be** later on **adjusted according to the needs** of specific project.

### Integrated tools

- **[uv](https://docs.astral.sh/uv/)** (python project manager)
- **[ruff](https://docs.astral.sh/ruff/formatter/)** (formatter)
- **[ruff](https://docs.astral.sh/ruff/linter/)** (linter)
- **[ty](https://docs.astral.sh/ty/)** (type checker)
- **[bandit](https://bandit.readthedocs.io/en/latest/)** (security checks)
- **[pytest](https://docs.pytest.org/en/7.1.x/contents.html)** (unit tests)
- **[pydantic](https://docs.pydantic.dev/latest/)** (data validation, models)
- **[pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** (settings management)
- **[prek](https://prek.j178.dev/)** (git hooks, running checks)
<!-- - **[devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)** (development inside container) -->


## Development

<!--
TODO devcontainer
####  a) Setup with devcontainer (recommended)
This template project uses devcontainer (VS code) to setup everything. So just follow [official documentation](https://code.visualstudio.com/docs/devcontainers/tutorial) to meet prerequisites. Then open this template project in container (using VS code) and you are ready to code!

#### b) Setup without devcontainer
-->

### Requirements

- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** - python project manager (*required*)
- **[make](https://www.gnu.org/software/make/manual/make.html)** - makefile, running commands (*recommended*)

### Setup

Install uv
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify uv installation
```sh
uv --version
```

---

Copy example env file
```sh
cp -n .env.example .env
```

Create new venv and sync packages (base + dev)
```sh
uv sync
```

Activate venv
```sh
. ./.venv/bin/activate
```


### Enable Prek - pre-commit git hook
[prek](https://prek.j178.dev/) configuration is enabled for this project. To run the hooks every time you commit, install prek’s git hook integration:

```sh
prek install
```


### Check and test code

On every commit code should be static tested/checked/formatted automatically (using [pre-commit](https://pre-commit.com/) tool).

You can run static checks using
```sh
make check
```

To run unit tests use
```sh
make test
```

<!-- ## Update packages
You can manually run a script that will check for new versions of packages which are used in this project. It will update both requirements files (`base.txt`, `dev.txt`).

On top of that there is a workflow added (`packages_update.yml`) that will create new Pull Request automatically with updated packages. Cronjob for this task is set for: `0 20 * * *` (every day - 20:00). -->

## Dockerize

<!-- There are two Dockerfiles in this project.

- `.devcontainer/Dockerfile`
- `Dockerfile`

First is for developing in a devcontainer and it's also used for running stuff in the pipeline. The second is for deploying the product as shown below. You should exclude unnecessary files (such as tests) using `.dockerignore` to keep the "production ready" container as ligthweight as possible. -->

Build `image`
```sh
docker build . --tag pyplate-image
```

Create `container` and run it
```sh
docker run pyplate-image
```

You can also use provided `docker-compose`
```sh
docker compose build
docker compose up
```
