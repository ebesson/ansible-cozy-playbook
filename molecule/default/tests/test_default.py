import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_common_packages(host):

    assert host.package("curl").is_installed
    assert host.package("net-tools").is_installed
    assert host.package("nginx").is_installed
    assert host.package("sudo").is_installed
    assert host.package("vim-tiny").is_installed
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

    cozy = host.service("cozy")
    assert cozy.is_running
    assert cozy.is_enabled
