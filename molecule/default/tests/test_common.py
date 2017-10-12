import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_common_packages(host):

    assert host.package("curl").is_installed
    assert host.package("apt-transport-https").is_installed
    assert host.package("vim").is_installed
