import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postfix_package(host):

    assert host.package("postfix").is_installed
    assert host.package("mailutils").is_installed


def test_postfix_service(host):
    postfix = host.service("postfix")
    assert postfix.is_running
    assert postfix.is_enabled
