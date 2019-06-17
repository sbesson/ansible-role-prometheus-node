Prometheus
==========

[![Build Status](https://travis-ci.org/ome/ansible-role-prometheus-node.svg)](https://travis-ci.org/ome/ansible-role-prometheus-node)
[![Ansible Role](https://img.shields.io/ansible/role/41324.svg)](https://galaxy.ansible.com/ome/prometheus_node/)

Prometheus node-exporter, defaults to listening on port 9100.


Role Variables
--------------

- `prometheus_node_args`: Arguments passed on the command line.
  See https://github.com/prometheus/node_exporter/ for configuration information.


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: ome.prometheus_node


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
