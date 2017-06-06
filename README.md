Prometheus
==========

Prometheus node-exporter, defaults to listening on port 9100.


Role Variables
--------------

- `prometheus_node_args`: Arguments passed on the command line.
  See https://github.com/prometheus/node_exporter/ for configuration information.


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: prometheus-node


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
