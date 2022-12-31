# basic-python-project-template
Template for a standard python project using github's CI/CD and devcontainers (VS code)

## Development

### Setup project

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
cd ./src/
black .
```

### Test code

* Linter (flake8)
```sh
cd ./src/
flake8
```

* Unit tests (pytest)
```sh
cd ./src/
python -m pytest tests/
```
