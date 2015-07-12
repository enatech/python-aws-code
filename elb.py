#!/usr/bin/env python

# Copyright (c) 2015 Nandini Taneja nandini.taneja@gmail.com
# All rights reserved.

import boto.ec2.elb
from boto.ec2.elb import HealthCheck

# get to my region in US East Coast
# AWS access and secret keys are in /etc/boto.cfg

regions = boto.ec2.regions()
myregion = regions[0]
conn = myregion.connect()
elb = boto.ec2.elb.connect_to_region(myregion)

#Create a ELB with port configuration and health checks
ports = [(80, 8080, 'http'), (443, 8443, 'tcp')]
hc = HealthCheck(
	interval=20,
	healthy_threshold=3,
	unhealthy_threshold=5,
	target='HTTP:8080/health'
)

lb = conn.create_load_balancer('nt-lb', zones, ports)
lb.configure_health_check(hc)

print "Load Balancer Created", lb.dns_name

#Add EC2 instabce to LB

reservations = conn.get_all_instances()

instance = reservation[0].instances
lb.register_instances(instance)

#remove instance
lb.deregister_instances(instance)
