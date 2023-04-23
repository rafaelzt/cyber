FROM alpine

ARG USER
ARG PASSWD

ENV USER=$USER
ENV PASSWD=$PASSWD

#
RUN apk update && \
	apk add openrc gpg nginx openssh tor && \
	rc-update add nginx && rc-update add sshd && rc-update add tor

# Setup
COPY ./config_files/setenv.sh /setenv.sh
COPY ./config_files/startup.sh /startup.sh
RUN  /setenv.sh && rm /setenv.sh

# NGINX
COPY ./config_files/default.conf /etc/nginx/conf.d/default.conf
COPY ./config_files/nginx.conf /etc/nginx/nginx.conf
COPY ./config_files/index.html /usr/share/nginx/html/index.html

# TOR
COPY ./config_files/torrc /etc/tor/torrc

# SSH
COPY ./config_files/sshd_config /etc/ssh/


EXPOSE 80
EXPOSE 4242
EXPOSE 9050


CMD ["/bin/sh", "/startup.sh"]
