export ANSIBLE_HOST_KEY_CHECKING=False;
/usr/bin/env ansible-playbook -i vagrant --private-key=/Applications/Vagrant/embedded/gems/gems/vagrant-1.6.3/keys/vagrant "$@"
