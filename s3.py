#!/usr/bin/env python

# Copyright (c) 2015 Nandini Taneja nandini.taneja@gmail.com
# All rights reserved.
import sys, getopt
import boto
from boto.s3.key import Key

# connect to Amazon S3
conn = boto.connect_s3()

def extract_file(fullpath):
	pos = fullpath.rfind("/")
	path = fullpath[pos+1:]
	return path

def create_bucket(b):
	# Create a bucket
	# Catch exception if the bucket can not be created or already exists
	print "Create a bucket:", b, " \n"

	try:
		conn.create_bucket(b)
	except S3CreateError as ce:
		print "Exception creating bucket: ", ce.errno
	else:
		print "Bucket created\n"

def upload_file(b,f):
	# Upload a file in the created bucket

	b = conn.get_bucket(b)
	k = Key(b)
	filename = extract_file(f)
	k.key = filename
	k.set_contents_from_filename(f)

	print "Uploaded file ", filename, "\n"

def delete_bucket(b):
	# Delete the bucket
	#conn.delete_bucket(b)
	print "Bucket", b, " deleted\n"

def main(argv):
	bucket = ''
	filename = ''
	if len(argv) < 2:
		print 's3.py <bucketname> <absolute filename>'
		sys.exit(2)
	bucket = argv[0]
	filename = argv[1]

	print "Bucket to create", bucket
	print "File to load ", filename

	# List all avaialble buckets in your account
	buckets = conn.get_all_buckets()
	length = len(buckets)

	# Total buckets
	print "Total: " , length , "buckets\n"

	print "Bucket Names @Amazon AWS and Contents\n"

	for b in buckets:
		print b.name
		print "\n"
		objects_in_b = b.list()
		for o in objects_in_b:
			print o.name

	create_bucket(bucket)
	upload_file(bucket,filename)
	#delete_bucket(bucket)
if __name__ == "__main__":
	main(sys.argv[1:])
