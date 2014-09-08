FROM ubuntu
MAINTAINER mrrrgn
RUN apt-get -y update
RUN apt-get install -y python-dev python-pip python-apt
RUN pip install ansible
ADD . /tmp/
WORKDIR /tmp/
RUN ansible-playbook -i local -c local webservers.yml
RUN sed -i "s/\[supervisord\]/\[supervisord\]\nnodaemon=true/" /etc/supervisor/supervisord.conf
EXPOSE 80
ENTRYPOINT ["/bin/bash"]
CMD ["/var/projects/poetry/scripts/start.sh"]
