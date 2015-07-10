#!/usr/bin/env python

# Copyright (c) 2015 Nandini Taneja nandini.taneja@gmail.com
# All rights reserved.

import boto.ec2

# connect to Amazon EC2
# AWS access and secret keys are in /etc/boto.cfg

regions = boto.ec2.regions()
myregion = regions[0]
conn = myregion.connect()

# List all avaialble instances
reservations = conn.get_all_instances()
length = len(reservations)

# Total instances
print "Total: " , length , "reservations\n"

#print "Instance Names @Amazon AWS and Contents\n"

for reservation in reservations:
	instance = reservation.instances
	print "Instance Id", instance
	print "Instance Type", instance.placement
	print "\n"

