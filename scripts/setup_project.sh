unset project_name

while read -p "[Required] Enter project name (without whitespaces): " project_name; do
     if [[ -z "${project_name}" ]]; then        # check if its empty value
          echo "Project name cannot be empty!"
     else
          echo "Creating ${project_name}..."
          break
     fi
done

read -p "[Optional] Enter author: " author
read -p "[Optional] Enter short description: " description

echo "# ${project_name}" > README.md

find . -type f -not \(      \
    -path "./venv/*" -o        \
    -path "./.git/*" -o        \
    -path "./imgs/*" -o        \
    -path "./scripts/*" -o     \
    -path "./logs/*"   -o      \
    -path "./requirements/*"   \
\) -exec sed -i "s/app-name/${project_name}/g" {} \;

find . -type f -path "./setup.py" -exec sed -i "s/__author__/${author}/g" {} \;
find . -type f -path "./setup.py" -exec sed -i "s/__description__/${description}/g" {} \;

rm -rf imgs/*

echo "Setup is done!"
