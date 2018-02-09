# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

$script = <<SCRIPT
pkill apt
apt-get install -y python
SCRIPT
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
 
  #config.vm.define "web1" do |web1|
		#web1.vm.box = "gbarbieru/xenial"
		#web1.vm.hostname = "web1"
		#web1.vm.network "public_network", :type => 'dhcp', :adapter => 2
	#	web1.ssh.password = "vagrant"
	#	web1.vm.provision :ansible do |ansible|
	#		ansible.playbook = "Webserver"
	#	end
 # end
  (1..2).each do |n|
	  config.vm.define "webservers#{n}" do |webservers|
			webservers.vm.box = "gbarbieru/xenial"
			webservers.vm.hostname = "web-server#{n}"
			webservers.vm.network "public_network", :type => 'dhcp', :adapter => 2
			webservers.ssh.password = "vagrant"
                        webservers.vm.provision "shell", inline: $script
			webservers.vm.provision :ansible do |ansible|
				ansible.playbook = "install_apache2.yml"
			end
	  end
  end
  
    config.vm.define "nginx" do |nginx|
		nginx.vm.box = "gbarbieru/xenial"
		nginx.vm.hostname = "nginx"
		nginx.vm.network "public_network", :type => 'dhcp', :adapter => 2
		nginx.ssh.password = "vagrant"
                nginx.vm.provision "shell", inline: $script
		nginx.vm.provision :ansible do |ansible|
			ansible.groups = {
			"nginx_servers" => ["nginx"],
			"web_servers" => ["webservers1","webservers2"]
			}
			ansible.limit = "all"
			ansible.playbook = "nginxLB.yml"
		end
  end
 # config.vm.define "" do |ansible|
	#	ansible.vm.box = "gbarbieru/xenial"
	#	ansible.vm.hostname = "Ansible"
	#	ansible.vm.network "public_network", :type => 'dhcp', :adapter => 2
	#	ansible.ssh.password = "vagrant"
	#	ansible.vm.provider "virtualbox" do |vb|
	#		vb.gui = true
	#	end
 # end

  
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end

