init:
	@echo "Initialize project setup"
	cp -n .env.example .env
	uv --version
	uv sync
	uv run prek install

check:
	@echo "Running static checks via prek (pre-commit hook)..."
	uv run prek run --all-files

test:
	@echo "Running unit tests..."
	uv run pytest --cov=pyplate --cov-report term-missing

run:
	@echo "Running python application..."
	uv run python3 ./pyplate/main.py

run-docker:
	@echo "Running containerized python application..."
	docker build . --tag pyplate-image
	docker run pyplate-image
