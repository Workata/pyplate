# basic-python-project-template
Template for a standard python project using github's CI/CD and devcontainers (VS code)

## Development

### Setup project

* Create/copy config file:
```sh
cp config_example.json config.json
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
