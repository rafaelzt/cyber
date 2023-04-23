#!/bin/sh

echo "##############################################################" > /dev/stdout
echo "" > /etc/init.d/hostname

# Create user
adduser -s /bin/sh -G root -H -D $USER > /dev/stdout
echo -e "$PASSWD\n$PASSWD" | passwd $USER > /dev/stdout

# Startup services
rc-service sshd start > /dev/stdout
sleep 2
# rc-service nginx start  > /dev/stdout
# sleep 1
rc-service tor start > /dev/stdout
sleep 1

cat /var/lib/tor/my_website/hostname > /etc/hostname
cat /etc/hostname > /dev/stdout
echo -e "$PASSWD" > /dev/stdout

echo "##############################################################" > /dev/stdout
nginx -g "daemon off;"