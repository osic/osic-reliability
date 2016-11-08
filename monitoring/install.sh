# Clone monitoring stack repository into /opt
git clone https://github.com/osic/reliability-openstack-ansible-ops.git /opt/reliability-openstack-ansible-ops

# Run the monitoring install script
cd /opt/reliability-openstack-ansible-ops/cluster_metrics
chmod +x install.sh
./install.sh 
