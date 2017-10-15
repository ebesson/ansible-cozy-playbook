import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cozy_stack_package(host):
    assert host.package("cozy-stack").is_installed


def test_cozy_service(host):
    cozy = host.service("cozy-stack")
    assert cozy.is_running
    assert cozy.is_enabled


def test_cozy_listen_ports(host):

    assert host.socket("tcp://127.0.0.1:8080").is_listening
    assert host.socket("tcp://127.0.0.1:6060").is_listening
