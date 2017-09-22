import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_package(host):
    assert host.package("nginx").is_installed


def test_ngnix_service(host):

    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_cozy_listen_ports(host):

    assert host.socket("tcp://0.0.0.0:443").is_listening
