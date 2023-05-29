echo "Check typing with mypy..."
mypy ./src/
echo "Format with Black..."
black ./src/
echo "Lint with flake8..."
flake8 ./src/
echo "Test with PyTest..."
python3 -m pytest ./src/tests/
