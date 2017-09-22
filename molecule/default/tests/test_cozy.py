import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cozy_service(host):
    cozy = host.service("cozy")
    assert cozy.is_running
    assert cozy.is_enabled


def test_cozy_directories(host):

    cozy_directories = [
        '/var/lib/cozy',
        '/etc/cozy'
        ]
    user_cozy = 'cozy'
    group_cozy = 'cozy'
    for cozy_directory in cozy_directories:
        assert host.file(cozy_directory).exists
        assert host.file(cozy_directory).is_directory
        assert host.file(cozy_directory).user == user_cozy
        assert host.file(cozy_directory).group == group_cozy


def test_cozy_listen_ports(host):

    assert host.socket("tcp://:::8080").is_listening
