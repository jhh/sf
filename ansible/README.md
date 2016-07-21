# Configuring Development Workstations

These instructions are used for our student loaner development laptops. We install [Ubuntu 16.04 LTS](http://www.ubuntu.com/desktop) and configure using [Ansible](http://docs.ansible.com/).

## Installation

1. Insert Ubuntu installation CD.
2. Press `ESC` for boot options. Select to boot from expansion bay.
3. When booted, select "Install Ubuntu".
4. Select "Install third-party software", leave "Download Updates" unchecked.
5. Select "Erase disk and Install Ubuntu" and "Use LVM", the rest unchecked.
6. Assign a hostname and record laptop serial number in spreadsheet.

## Post Installation

1. Log in directly and `sudo apt install openssh-server`.
2. From the Ansible control host, run `ssh-copy-id <admin>@<hostname>.local`.
3. Log in with ssh and `sudo apt dist-upgrade` and reboot.
4. Log in with ssh and `sudo -s cp -R --preserve=mode ~/.ssh /root/` to allow Ansible to operate as root.

## Bootstrapping Ansible

1. Add new host to [`inventory`](inventory) file.
2. Ping new host with `ansible -i inventory -m ping <host>`.
3. In `sf/ansible`, run `ansible-playbook -i inventory site.yml`


## Ansible Tips
- To run the playbook on a single host, run `ansible-playbook -i inventory site.yml -l <host>`.
- To exclude a host, run `ansible-playbook -i inventory site.yml -l '!<host>'`
- To add a user, run
  ```sh
  $ python3 -c "from passlib.hash import sha512_crypt; import getpass; print(sha512_crypt.encrypt(getpass.getpass()))"
  $ ansible -i inventory -m user -a 'name=johnd comment="John Doe" password="<crypted password>" shell=/bin/bash' <host>
  ```
