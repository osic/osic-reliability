Gather and visualize cluster wide metrics
#########################################

About this repository
---------------------

Code was forked from: https://github.com/openstack/openstack-ansible-ops/tree/master/cluster_metrics
Special thanks to the repository contributors for making this possible.

Install
-------

Before starting you should have an OpenStack ansible deployment working.

If you have a multinode installation please do the following:

.. code-block:: bash
   mv etc/env.d/cluster_metrics_multinode.yml etc/env.d/cluster_metrics.yml

If you have an all in one deployment do:

.. code-block:: bash
   mv etc/env.d/cluster_metrics_aio.yml etc/env.d/cluster_metrics.yml

Run the install script

.. code-block:: bash

   ./install.sh

If you are using HA proxy run:

.. code-block:: bash

   ./install.sh -e


