read -p "[Required] Enter project name (without whitespaces): " project_name
read -p "[Optional] Enter author: " author
read -p "[Optional] Enter short description: " description

echo "# ${project_name}" > README.md

find . -type f -not \(      \
    -path "./venv/*" -o     \
    -path "./.git/*" -o     \
    -path "./imgs/*" -o     \
    -path "./scripts/*" -o  \
    -path "./logs/*"   -o  \
    -path "./requirements/*"   \
\) -exec sed -i "s/app-name/${project_name}/g" {} \;

echo "Setup is done!"
