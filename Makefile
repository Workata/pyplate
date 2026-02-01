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
	@echo "Running fast api application..."
	uv run uvicorn pic_back.main:app --host 0.0.0.0 --port 8000


.PHONY: run-docker
run-docker:
	@echo "Running containerized fast api application..."
	docker build . --tag pic-back-image
	docker run pic-back-image
