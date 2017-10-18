# Ansible playbook for Cozy v3
This playbook allow to install a full Cozy v3. The following roles are provide:

- common: install base package and cozy repository
- couchdb: install and configure cozy-couchdb
- cozy: install and configure cozy-stack
- nginx: install and configure nginx
- cozy-coclyco: install cozy-coclyco


For more information, see Cozy documentation: https://docs.cozy.io/en/install/debian/


### Developpement status
[![Build Status](https://travis-ci.org/ebesson/ansible-cozy-playbook.svg?branch=master)](https://travis-ci.org/ebesson/ansible-cozy-playbook.svg?branch=master)


### License
AGPL v3 license.