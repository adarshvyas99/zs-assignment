Problem: Automate the workflow for preparing a host.

Goal: Create an Ansible script that provisions an Ubuntu server 22.04 with the following
components. Applications should be installed with rootless Podman containers running as
unprivileged user app (unless stated otherwise).

Subtasks:
1. Ansible script should not expect to be root on the destination but should use sudo
2. You can use this project as a reference (it is using rootless Podman containers with
Systemd, sets up Prometheus, Wireguard, a firewall for using privileged ports [in the ingress
role] and various apps in the compose directory (i.e. grafana, healthchecks). ):
https://github.com/brettinternet/homelab
3. Use and commit a locally defined Vagrantfile configuration for easy testing and
developing: https://www.vagrantup.com/docs/provisioning/ansible
4.MOTD should be configurable
5. Block all ports except SSH, email, HTTP, VPN, BigBlueButton ports, AdGuardHome ports
( 53/tcp , 67/udp , 853/tcp , 784/udp , 5443/tcp ) and GitLab (Git+SSH, HTTP[S] and Docker
registry) ports via firewall.
6. Additionally, write a flask app in Python to trigger ansible run using API.