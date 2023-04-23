#!/bin/sh

openrc
touch /run/openrc/softlevel

mkdir -p /root/.ssh/
mkdir -p /usr/share/nginx/html/
mkdir -p /var/lib/tor/my_website/

chown tor -R /var/lib/tor/my_website
chmod 700 -R /var/lib/tor/my_website

