import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_common_packages(host):

    assert host.package("curl").is_installed
    assert host.package("net-tools").is_installed
    assert host.package("sudo").is_installed
    assert host.package("build-essential").is_installed
    assert host.package("pkg-config").is_installed
    assert host.package("erlang").is_installed
    assert host.package("libicu-dev").is_installed
    assert host.package("libmozjs185-dev").is_installed
    assert host.package("libcurl4-openssl-dev").is_installed


def test_couchdb(host):

    couchdb = host.service("couchdb")
    assert couchdb.is_running
    assert couchdb.is_enabled


def test_cozy(host):

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

    cozy = host.service("cozy")
    assert cozy.is_running
    assert cozy.is_enabled


def test_ngnix(host):

    assert host.package("nginx").is_installed
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled
    assert host.socket("tcp://0.0.0.0:443").is_listening
