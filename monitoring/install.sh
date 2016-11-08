# Clone monitoring stack repository into /opt
cd opt
git clone https://github.com/osic/reliability-openstack-ansible-ops.git

# Run the monitoring install script
./reliability-openstack-ansible-ops/cluster_metrics/install.sh 
