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
- **[pre-commit](https://pre-commit.com/)**
- **[devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)**

## TODOs for developer after using this template

- [ ] Find and replace all occurrences of 'app-name' to your project name phrase.
- [ ] Open `setup.py` and update information about the project like Author, Description etc.
- [ ] Adjust (remove/add) tools and related configs according to your needs


## Things you would want to add

### Poetry

[Poetry](https://python-poetry.org/) can help you with packaging and dependency management.


<!-- ## Development -->

## Setup project

####  With devcontainer (recommended)
This template project uses devcontainer (VS code) to setup everything. So just follow [official documentation](https://code.visualstudio.com/docs/devcontainers/tutorial) to meet prerequisites. Then open this template project in container (using VS code) and you are ready to code!

#### Without devcontainer

Copy env file
```sh
cp -n .env.example .env
```

Create new venv
```sh
python3 -m venv ./venv
```

Install needed requirements
```sh
pip install -r requirements/dev.txt
```

Run unit tests to check if it works
```sh
pytest ./src/
```



## Test code

On every commit code should be static tested/checked/formatted automatically (using [pre-commit](https://pre-commit.com/) tool). If you want to run static tests + unit tests run:

```sh
./scripts/run_tests.sh
```
