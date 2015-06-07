# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Get rid of that pesky "stdin: is not a tty" error
    config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

    # Hashicorp standard Ubuntu 12.04 LTS 64-bit box
    config.vm.box = "oakensoul/ansible-citadel"

    # Configure port forwarding
    config.vm.network "forwarded_port", guest: 80, host: 80
    config.vm.network "forwarded_port", guest: 443, host: 443

    # Forward SSH keys to the Guest VM
    config.ssh.forward_agent = true

end
