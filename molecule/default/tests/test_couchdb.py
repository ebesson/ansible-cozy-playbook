import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_couchdb_package(host):
    assert host.package("cozy-couchdb").is_installed


def test_couchdb_service(host):

    couchdb = host.service("couchdb")
    assert couchdb.is_running
    assert couchdb.is_enabled


def test_couchdb_listen_ports(host):

    assert host.socket("tcp://127.0.0.1:5986").is_listening
    assert host.socket("tcp://127.0.0.1:5984").is_listening
