# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# this script is used to install python on the target servers becuase ansible is needed
$script = <<SCRIPT
pkill apt
apt-get install -y python
SCRIPT
Vagrant.configure("2") do |config|
	# Create Apache Servers
  (1..2).each do |n|
	  config.vm.define "apache_server#{n}" do |apache_server|
		  apache_server.vm.box = "gbarbieru/xenial"
		  apache_server.vm.hostname = "apacheserver#{n}"
		  apache_server.vm.network "public_network", :type => 'dhcp', :adapter => 2
		  apache_server.ssh.password = "vagrant"
		  apache_server.vm.provision "shell", inline: $script
		  apache_server.vm.provision :ansible do |ansible|
			ansible.playbook = "playbooks/install_apache2.yml"
		  end
	  end
  end
	# Create Nginx Servers
    config.vm.define "nginx_server" do |nginx_server|
	nginx_server.vm.box = "gbarbieru/xenial"
	nginx_server.vm.hostname = "nginx"
	nginx_server.vm.network "public_network", :type => 'dhcp', :adapter => 2
	nginx_server.ssh.password = "vagrant"
        nginx_server.vm.provision "shell", inline: $script
	nginx_server.vm.provision :ansible do |ansible|
		ansible.groups = {
		"nginx_servers" => ["nginx_server"],
		"apache_servers" => ["apache_server1","apache_server2"]
		}
		ansible.limit = "all"
		ansible.playbook = "playbooks/install_nginx.yml"
	end
    end
end

