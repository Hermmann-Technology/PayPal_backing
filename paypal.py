#!/bash/sh
echo -n  "Please enter username"
read username
echo -n "Enter password"
read -s password
sudo adduser $username
echo "password |sudo passwd" $username --stdin
