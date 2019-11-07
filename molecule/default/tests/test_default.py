import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_services_running_and_enabled(host):
    assert host.service('prometheus-node-exporter').is_running
    assert host.service('prometheus-node-exporter').is_enabled


def test_node_exporter_metrics(host):
    out = host.check_output('curl http://localhost:19100/metrics')
    assert 'process_cpu_seconds_total' in out
