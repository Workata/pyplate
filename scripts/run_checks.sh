echo "Check typing with mypy..."
mypy ./src/

echo "Format with Black..."
black ./src/

echo "Lint with flake8..."
flake8 ./src/

echo "Test with PyTest... (+ check coverage)"
coverage run -m pytest ./src/

echo "Report coverage..."
coverage report -m
