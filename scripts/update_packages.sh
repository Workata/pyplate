echo "Updating packages in requirements/base.txt file..."
pur -r requirements/base.txt
echo "Updating packages in requirements/dev.txt file..."
pur -r requirements/dev.txt
echo "Commit your changes only if all tests are passing!"
echo "Verify with: pytest ./src/"
