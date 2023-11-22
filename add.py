#!/bash/sh
#This is to create a user
#You must be root before running thing this task

echo -n "Enter your username"
read username
sudo useradd $username
echo -n "Enter your password for yopur account to be created"
read -s password
echo "accont created successfully"
