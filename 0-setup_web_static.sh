#!/usr/bin/env bash
#Install Nginx if not already installed
apt-get update
apt-get -y install nginx

#Recursively create directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

#Create a fake HTML file
echo "Happy to be here!" | tee /data/web_static/releases/test/index.html > /dev/null

#Create a symbolic link, and deletes it if it already exists
ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give /data/ ownership to user and group
chown -R ubuntu:ubuntu /data/

#Update Nginx configuration
if ! grep -q "hbnb_static" /etc/nginx/sites-available/default; then
	sed -i "/server_name _;/a \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
fi

#Restart Nginx
service nginx restart
