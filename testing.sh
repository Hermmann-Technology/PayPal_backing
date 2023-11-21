#!/bash/sh
#This is to creat an account for a particular user
#you have to be root before caring out this task
#This following commands should be run a linuxs saver
author: Jason 

echo "Please enter your username"
read username
sudo useradd $username
echo "Please enter your password for your account to be created"
read  password
sudo passwd $username
