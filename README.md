# osic-reliability
# Overview
__more notes in Google Doc__

High Availability of Services
Teams/Projects: Ops, Docs, Tech Marketing
Designated Tech Lead:  Melvin
Designated Group Coordinator:
Why: Enterprises have concerns about the availability of OpenStack, specifically at scale.
Details: Verification Process, test and publish what works. 
Projects Deployed: 
Nova, Neutron, Glance, Cinder, Keystone, Swift, Ironic
Potential process:
Define what we mean by available
Is it Operational (Synthetic Build)
Is it Service Response (Ping API)
Define, review and approve  process for measuring control plane availability
Start with Rackspace MaaS Remote Monitoring
https://github.com/rcbops/rpc-openstack/tree/master/maas/plugins
Define, review and approve workload
Start with Rackspace Private Cloud generic customer workload, or OpenStack Infra
Document the recipe for the results, how did we get this data, scientific method we used
Four different three week deploys at 10,100,500,1000
Deploy OpenStack Newton
Deploy workloads 
Measure control plane availability under workload for three weeks
Publish results to the community
Success Criteria: Four published papers, one at each scale size
User Story
Epic Name:
Trello Card:
