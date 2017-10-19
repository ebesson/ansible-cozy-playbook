# Ansible playbook for Cozy v3
This playbook allow to install a full Cozy v3. The following roles are provide:

- common: install base package and cozy repository
- couchdb: install and configure cozy-couchdb
- cozy: install and configure cozy-stack
- nginx: install and configure nginx
- cozy-coclyco: install cozy-coclyco


For more information, see Cozy documentation: https://docs.cozy.io/en/install/debian/

### Roadmap
- [ ] Manage cozy instances from playbook
- [ ] Check the playbook on Xenial

### Developpement status
[![Build Status](https://travis-ci.org/ebesson/ansible-cozy-playbook.svg?branch=master)](https://travis-ci.org/ebesson/ansible-cozy-playbook.svg?branch=master)


### How to use this playbook
#### Settings your Cozy configuration
- Edit the inventory file `inventories/cozy`, and add your server
- Define your secrets on the vault file `group_vars/cozy/vault`
- Encrypt your secrets with the following command :
```bash
ansible-vault encrypt group_vars/cozy/vault
```

### Launch the playbook
So as to deploy your Cozy instance on your server, launch the following command :
```bash
ansible-playbook -i inventories/cozy cozy.yml \
      --ask-vault-pass \
      --ask-pass \
      --ask-become-pass \
      --user=YOUR_SSH_USER
```


### License
AGPL v3 license.