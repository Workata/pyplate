.PHONY: check
check:
	@echo "Running static checks via prek (pre-commit hook)..."
	uv run prek run --all-files

.PHONY: test
test:
	@echo "Running unit tests..."
	uv run pytest --cov=pyplate --cov-report term-missing

.PHONY: run
run:
	@echo "Running python application..."
	uv run python3 ./pyplate/main.py

.PHONY: run-docker
run-docker:
	@echo "Running containerized python application..."
	docker build . --tag pyplate-image
	docker run pyplate-image
