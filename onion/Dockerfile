FROM alpine

RUN apk update && \
	apk add openrc gpg nginx openssh tor && \
	rc-update add nginx && rc-update add sshd && rc-update add tor

COPY ./config_files/setenv.sh /setenv.sh
RUN  /setenv.sh

COPY ~/id_rsa.pub ~/.ssh/authorized_keys
COPY ./config_files/default.conf /etc/nginx/conf.d/default.conf
COPY ./config_files/nginx.conf /etc/nginx/nginx.conf
COPY ./config_files/torrc /etc/tor/torrc
COPY ./config_files/hostname /etc/init.d/hostname
COPY ./config_files/sshd_config /etc/ssh/sshd_config

EXPOSE 80
EXPOSE 4242
EXPOSE 9050


CMD ["/bin/sh"]
